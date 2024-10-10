### Just testing new Prefect 3.0 functionality

---

Select and push deployment from file:
```bash
prefect deploy flows\check_table\deployment.yaml
```
Push **all** deployments from file:
```bash
prefect deploy --prefect-file flows\check_table\deployment.yaml --all
```
Disable prompts:
```bash
prefect --no-prompt deploy --prefect-file flows\check_table\deployment.yaml --all
```

---

Upgrade to Prefect 3: https://docs.prefect.io/3.0/resources/upgrade-to-prefect-3

After prefect package version is upgraded:
```bash
prefect server database upgrade
```
