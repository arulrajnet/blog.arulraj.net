

```dataview
table title, category, tags
from "content"
where status = null or status!="draft"
sort date desc
```