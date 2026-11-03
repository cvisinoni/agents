# SQL (Oracle)

The project rules and specifications in `.agents/project/` take precedence over this file.

## Query formatting

- Write SQL keywords (`SELECT`, `FROM`, `WHERE`, `JOIN`, `INSERT`, `UPDATE`, etc.) in uppercase, and identifiers and functions (`count`, `sum`, `coalesce`, `to_date`, etc.) in lowercase.
- Start every clause (`SELECT`, `FROM`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, etc.) at the beginning of the line, without right-aligning them.
- If the `SELECT` has at least two fields, break the line after `SELECT` and write one indented field per line; with a single field write `SELECT field` on the same line.
- If at least one field of the `SELECT` has an alias, give an alias to all fields (with `AS`) and align the aliases vertically, leaving at least 4 spaces after the longest field.
- If the `ORDER BY` has at least two fields, break the line after `ORDER BY` and write one indented field per line; with a single field write `ORDER BY field` on the same line.
- Use explicit ANSI JOINs; do not use the `(+)` syntax.
- If the query involves at least two tables, break the line after `FROM` and write tables and `JOIN`s one per line, indented; with a single table write `FROM table` on the same line.
- If the `WHERE` has at least two conditions, break the line after `WHERE` and write each condition on its own indented line, with `AND`/`OR` at the start of the line; with a single condition write `WHERE condition` on the same line.
- Write `ON` and all its conditions (even with multiple `AND`s) on the same line as the `JOIN`.
- Vertically align the table aliases in the `FROM`, leaving at least 4 spaces after the longest name (with `JOIN`), and also align the `ON`s by adding spaces after the shorter aliases.
- For a subquery in a `JOIN`, open the parenthesis on the `JOIN` line, indent the content by one level and close with `)` followed, on the same line, by the alias aligned with the others and the `ON`.
- Qualify columns with the table alias in queries that involve multiple tables and choose clear aliases.

Example of a complex query:

```sql
WITH order_totals AS (
    SELECT
        o.customer_id          AS customer_id,
        count(*)               AS orders_count,
        sum(r.order_amount)    AS total_amount
    FROM
        orders             o
        JOIN order_rows    r ON r.order_id = o.order_id
    WHERE
        o.order_date >= to_date('2024-01-01', 'YYYY-MM-DD')
        AND o.status = 'CONFIRMED'
    GROUP BY o.customer_id
)
SELECT
    c.customer_id                  AS customer_id,
    c.customer_name                AS customer_name,
    t.orders_count                 AS orders_count,
    t.total_amount                 AS total_amount,
    lo.last_order_date             AS last_order_date,
    coalesce(a.city, 'N/A')        AS city
FROM
    customers              c
    JOIN order_totals      t  ON t.customer_id = c.customer_id
    LEFT JOIN addresses    a  ON a.customer_id = c.customer_id AND a.address_type = 'BILLING'
    LEFT JOIN (
        SELECT
            o.customer_id        AS customer_id,
            max(o.order_date)    AS last_order_date
        FROM orders o
        GROUP BY o.customer_id
    )                      lo ON lo.customer_id = c.customer_id
WHERE
    c.status = 'ACTIVE'
    AND t.total_amount > 1000
ORDER BY
    t.total_amount DESC,
    c.customer_name;
```

## Views

- ALWAYS create views as `NONEDITIONABLE`: use `CREATE OR REPLACE NONEDITIONABLE VIEW`, never `EDITIONABLE` nor the form without the attribute.

```sql
CREATE OR REPLACE NONEDITIONABLE VIEW active_customers_v AS
SELECT
    c.customer_id      AS customer_id,
    c.customer_name    AS customer_name
FROM customers c
WHERE c.status = 'ACTIVE';
```

## Query syntax

- Do not use `SELECT *` in application code: select only the necessary columns.
- Convert strings to dates with `to_date` and an explicit format.
- Avoid implicit type and date conversions.
- Do not use hints without a motivation verified on the execution plan.
- Avoid functions applied to indexed columns in filter conditions, unless function-based indexes are available.

```sql
SELECT count(*)
FROM orders
WHERE order_date >= to_date('2024-01-01', 'YYYY-MM-DD');
```
