# Softwood Log

Raw, unrefined wood. Will need a carpenter's attention to get it into a usable state.

## In the game

Raw, unrefined wood. Will need a carpenter's attention to get it into a usable state.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | wood_log |
| Item type | Forest |
| Resource Value | 200 |
| Worker Type | Logger |
| Workers Per Item | 4 |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Forest](building-Forest.md) | [Harvest Wood Log](tech-forest_wood_log.md) | 1.0 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Softwood Plank](recipe-wood_plank.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_13\"",
  "ResourceValue": "200L",
  "WorkerType": "ForestWorker.Logger",
  "WorkersPerItem": "4.0"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier4.cs:10`
