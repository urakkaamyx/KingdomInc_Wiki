# Compounding Effort

Quest duration increases for each time this quest has been completed previously.

## Effect

Quest duration increases for each time this quest has been completed previously.

## Appears on quests

| Quest |
| --- |
| [Mine Sweep](quest-clear_mines.md) |
| [Wilderness Evangelism](quest-forest_evangelism.md) |

## Properties

| Property | Value |
| --- | --- |
| Triggered | false (default) |
| Trigger chance | 0.05f (default, applies only to triggered challenges) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_203\"",
  "Label": "\"@quest_challenge_increase_duration\"",
  "Description": "\"@quest_challenge_increase_duration_desc\""
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:89`
