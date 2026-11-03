# PL/SQL (Oracle)

The project rules and specifications in `.agents/project/` take precedence over this file.

## SQL inside PL/SQL (mandatory)

**Every SQL query written inside PL/SQL code must follow `~/.agents/coding/sql.md` in full.** Read that file before writing or changing any PL/SQL unit that contains SQL.

- This applies to all embedded SQL: `SELECT ... INTO`, cursor queries (including `for rec in (...) loop`), `INSERT`, `UPDATE`, `DELETE`, `MERGE`, subqueries, and SQL held in dynamic SQL strings.
- Query formatting, keyword case, alias alignment, ANSI JOINs, `to_date` with explicit formats, no `SELECT *`, and the other rules of `sql.md` have the same weight here as in plain SQL scripts.
- The PL/SQL case and formatting rules below apply to the PL/SQL statements around the query, not to the query itself.
- If this file and `sql.md` seem to disagree about how a query is written, `sql.md` wins for the query.

## Goals and general conventions

- Write clear, consistent, readable and maintainable code, simple and explicit, avoiding duplication.
- Use technical names generally in English and comments generally in Italian.
- Check the database version (e.g. 19c, 23ai, Autonomous) before using recent features.
- Use the deployment and migration tools already adopted by the project (e.g. Liquibase, Flyway, numbered scripts).

## Naming

| Element | Convention |
|---|---|
| Identifiers | lowercase, descriptive, in `snake_case` |
| Local variables | `v_` prefix |
| Input parameters | `p_` prefix |
| Output parameters | `x_` prefix |
| Package global variables | `g_` prefix |
| Constants | `c_` prefix |
| Packages | `_pkg` suffix |
| Views | `_v` suffix |
| Sequences | `_s` suffix |

- Follow the prefixes already present in the schema, keeping the conventions for variables, parameters, globals and constants indicated above distinct.
- Choose descriptive names; avoid generic names such as `v_tmp`, `v_value` and `v_data`.
- Avoid reserved words and identifiers in double quotes.
- Use the `_pkg` suffix for packages and choose a name that describes the functional domain, for example `customer_pkg` or `invoice_pkg`.
- Use the `_s` suffix for sequences of technical identifiers, for example `customer_id_s` or `async_job_s`.

## Case and formatting

- Write PL/SQL control keywords in lowercase: `for`, `loop`, `if`, `then`, `else`, `elsif`, `end if`.
- Write `BEGIN` and `END unit_name` in uppercase for the start and end of blocks and units; control closings such as `end if` stay lowercase.
- Use 4-space indentation, one logical statement per line and blank lines to separate logical blocks.
- Align parameters and assignments when it improves readability.
- Terminate every SQL and PL/SQL statement with `;` and packages, procedures and functions with `END unit_name;`.
- In SQL*Plus/SQLcl scripts, add `/` after PL/SQL blocks.

## Package specification

The package specification exposes only what is needed externally.

- Declare only the public procedures, functions, types and constants that are needed.
- Do not put comments or implementations in the specification.
- Do not use `%TYPE` or `%ROWTYPE` parameters derived from tables in the specification.
- Use explicit types for public parameters: `NUMBER`, `VARCHAR2`, `DATE`, `CLOB`.

```sql
CREATE OR REPLACE PACKAGE customer_pkg AS
    PROCEDURE create_customer (
        p_customer_name    IN VARCHAR2,
        p_birth_date       IN DATE,
        x_customer_id      OUT NUMBER
    );
END customer_pkg;
/
```

## Package body and PL/SQL units

- Group the logic in packages; avoid standalone procedures and functions.
- The package body contains the implementations and the comments. Every procedure or function must be preceded by the standard comment below.
- Keep the comments before procedures and functions in the body; do not put them in the specification.
- Split the logic into clear blocks and end every procedure or function with its own name.
- Declare variables at the beginning of the `AS` section.
- Parameters use `p_` for input and `x_` for output; local variables use `v_`.

Comment format for a procedure:

```sql
/**
 * --------------------------------------------------------------------------------------------------------------------------
 * PROCEDURE procedure_name
 * --------------------------------------------------------------------------------------------------------------------------
 * Brief description of the procedure.
 *
**/
```

For a function, replace `PROCEDURE` with `FUNCTION`.

## Parameters and variables

- Use explicit types for parameters and align them for readability.
- For local variables, use `%TYPE` and `%ROWTYPE` when appropriate; `%TYPE` is useful to align with the type of a column.
- Keep the public parameters of the specification explicit and independent of table types.

```sql
PROCEDURE calculate_total_amount (
    p_order_id       IN NUMBER,
    x_total_amount   OUT NUMBER
) AS
    v_total_amount   orders.total_amount%TYPE;
BEGIN
    SELECT sum(order_amount)
    INTO v_total_amount
    FROM order_rows
    WHERE order_id = p_order_id;

    x_total_amount := coalesce(v_total_amount, 0);
END calculate_total_amount;
```

Example with more than one field:

```sql
SELECT
    c.customer_name,
    c.status
INTO
    v_customer_name,
    v_status
FROM customers c
WHERE c.customer_id = p_customer_id;
```

## Queries and cursors

- Format every query according to `~/.agents/coding/sql.md` (see "SQL inside PL/SQL (mandatory)" above).
- In `SELECT ... INTO`, the `INTO` clause follows the same rule as the `SELECT` fields: with at least two variables, break the line after `INTO` and write one indented variable per line; with a single variable write `INTO variable` on the same line.
- Prefer set-based SQL operations over row-by-row loops.
- When iteration is necessary, prefer the implicit cursor `for rec in (...) loop`; avoid explicit cursors unless really needed.
- Use `BULK COLLECT` and `FORALL` when iterative processing is necessary and the volume justifies it.
- Move long, complex or reused queries into views with the `_v` suffix. ALWAYS create views as `NONEDITIONABLE` (`CREATE OR REPLACE NONEDITIONABLE VIEW`), as required by `~/.agents/coding/sql.md`.
- Explicitly handle cases with no results and, when necessary, `NULL` values using `nvl`, `coalesce` or explicit checks.

```sql
for rec in (
    SELECT
        c.customer_id,
        c.customer_name
    FROM customers c
    WHERE c.status = 'ACTIVE'
) loop
    update_customer_score(rec.customer_id);
end loop;
```

## Dates

- Use `DATE`; do not use `TIMESTAMP` unless there is an explicit technical or functional request.
- For the current date use `SYSDATE`.

```sql
v_creation_date := SYSDATE;
```

## Error handling and transactions

- Handle only the expected exceptions for which a sensible action exists.
- Do not use `WHEN OTHERS THEN NULL`; if you use `WHEN OTHERS`, log the error and re-raise it with `RAISE`.
- Use `RAISE_APPLICATION_ERROR` with codes in the range `-20000` to `-20999` and clear messages.
- Do not execute `COMMIT` or `ROLLBACK` in reusable units: the transaction is governed by the caller.

## Security

- Use bind variables; do not concatenate input into dynamic SQL statements.
- If dynamic SQL is unavoidable, validate identifiers with `DBMS_ASSERT`.
- Grant the minimum necessary privileges and evaluate `AUTHID CURRENT_USER` versus `AUTHID DEFINER`.
- Do not put credentials or personal data in scripts.

## Tests and performance

- Use the project's test framework (e.g. utPLSQL); in its absence, provide repeatable verification scripts.
- Verify the cases with missing data, `NULL` values, duplicates and high volumes.
- For critical queries, check the execution plan with `DBMS_XPLAN`.

## Operations to avoid

- Do not execute destructive DDL or DML (`DROP`, `TRUNCATE`, `DELETE` without `WHERE`) without an explicit request.
