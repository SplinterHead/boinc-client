## Project Operations
These operations are for interacting with Projects

### Attach Project
```python
boinc_client.attach_project()
```

#### Arguments
| Argument | Description                                | Required | Default |
|----------|--------------------------------------------|----------|---------|
| `name`   | Name of the project to join                | Yes      | None    |
| `url`    | URL of the project to join                 | Yes      | None    | 
| `key`    | Authentication key for joining the project | Yes      | None    |

Response
```python
{
    "success": False,
    "error": "Failed to attach to project"
}
```

### Poll Project Attach
```python
boinc_client.poll_attach_project()
```

Response
```python
{
    "project_attach_reply": {
        "messages": ["Failed to connect"],
        "error_num": 1
    }
}
```

### Update Project
```python
boinc_client.update_project()
```

#### Arguments
| Argument | Description                       | Required | Default |
|----------|-----------------------------------|----------|---------|
| `url`    | URL of the project to detach from | Yes      | None    |

Response
```python
{
    "success": False,
    "error": "Failed to detach from project"
}
```

### Detach Project
```python
boinc_client.detach_project()
```

#### Arguments
| Argument | Description                       | Required | Default |
|----------|-----------------------------------|----------|---------|
| `url`    | URL of the project to detach from | Yes      | None    | 

Response
```python
{
    "success": False,
    "error": "Failed to detach from project"
}
```