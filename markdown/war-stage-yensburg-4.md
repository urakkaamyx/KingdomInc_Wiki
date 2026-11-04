# Throne Room

Stage 4 of Siege of Yensburg.

## Description

At the heart of the castle lies the throne room, a shining beacon of Yensburg's authority. The enemy has barricaded themselves there, clearly engaged in some sinister plot.

## Reward Description

Retake the Throne Room to be crowned King, and begin your assault on the enemy stronghold!

## Reward Complete

Hail to the King, baby!

## Campaign parameters

| Parameter | Amount |
| --- | --- |
| Progress Amount | 250 |
| Enemy Damage | 44 |
| Start Strength | 13000 |
| End Strength | 14000 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@war_yensburg_stage_4\"",
  "Description": "\"@war_yensburg_stage_4_desc\"",
  "RewardDescription": "\"@war_yensburg_stage_4_reward\"",
  "RewardComplete": "\"@war_yensburg_stage_4_reward_2\"",
  "IconName": "\"Icons2_60\"",
  "ProgressAmount": "250",
  "EnemyDamage": "44",
  "StartStrength": "13000",
  "EndStrength": "14000",
  "OnComplete": "() =>\n\t\t\t\t\t{\n\t\t\t\t\t\tSteamAchievement.Trigger(\"WarYensburg\");\n\t\t\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Wars/Yensburg.cs:9`
