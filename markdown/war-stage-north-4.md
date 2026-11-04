# Pinnacle Ruins

Stage 4 of Ironcrag Siege.

## Description

At the top of the mountain, a hidden path leads past the caldera and down into the earth. The enemy's stronghold has been exposed.

## Reward Description

Conquer the Pinnacle Ruins in order to descend into the Tomb of Sholrath.

## Reward Complete

The path to the Tomb has been breached!

## Campaign parameters

| Parameter | Amount |
| --- | --- |
| Progress Amount | 250 |
| Enemy Damage | 47 |
| Start Strength | 19000 |
| End Strength | 21000 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@war_north_stage_4\"",
  "Description": "\"@war_north_stage_4_desc\"",
  "RewardDescription": "\"@war_north_stage_4_reward\"",
  "RewardComplete": "\"@war_north_stage_4_reward_2\"",
  "IconName": "\"Icons2_74\"",
  "ProgressAmount": "250",
  "EnemyDamage": "47",
  "StartStrength": "19000",
  "EndStrength": "21000",
  "OnComplete": "() =>\n\t\t\t\t\t{\n\t\t\t\t\t\tSteamAchievement.Trigger(\"WarNorth\");\n\t\t\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Wars/North.cs:9`
