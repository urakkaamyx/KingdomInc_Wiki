# Bastion

Stage 4 of Orcish Horde.

## Description

The fortress-city of Bastion was founded after the first expedition into the Hinterlands, centuries ago. The surrounding territory was subsequently conquered by orcs, but the city still defiantly maintains a human population.

## Reward Description

Retake Bastion to regain access to its Arena!

## Reward Complete

Arena tech unlocked!

## Campaign parameters

| Parameter | Amount |
| --- | --- |
| Progress Amount | 250 |
| Enemy Damage | 36 |
| Start Strength | 8000 |
| End Strength | 10000 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@war_east_stage_4\"",
  "Description": "\"@war_east_stage_4_desc\"",
  "RewardDescription": "\"@war_east_stage_4_reward\"",
  "RewardComplete": "\"@war_east_stage_4_reward_2\"",
  "IconName": "\"Icons_177\"",
  "ProgressAmount": "250",
  "EnemyDamage": "36",
  "StartStrength": "8000",
  "EndStrength": "10000",
  "OnComplete": "() =>\n\t\t\t\t\t{\n\t\t\t\t\t\tSteamAchievement.Trigger(\"WarEastern\");\n\t\t\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Wars/East.cs:9`
