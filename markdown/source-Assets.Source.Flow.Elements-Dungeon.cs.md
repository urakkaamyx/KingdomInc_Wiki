# Dungeon — source reference

Assets.Source.Flow.Elements/Dungeon.cs · 270 lines · 2 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class Dungeon : FlowElement |
| 19 | public const float DungeonTickTime = 2f |
| 21 | public DungeonProgress CurrentDungeon |
| 23 | public bool TriggerAttack |
| 31 | public bool LimitBreak |
| 33 | public bool LimitBreak2 |
| 35 | public float CoinLootMultiplier = 1f |
| 37 | public override string Label => "@dungeon" |
| 39 | public override ElementCategory Category => ElementCategory.Consumption |
| 41 | public override string IconName => "Icons_195" |
| 43 | public override Sprite Icon => CurrentDungeon?.Dungeon.Icon ?? base.Icon |
| 45 | public override string MusicTrack => "Temple Explore LOOP BPM110" |
| 47 | public int TrashLoot { get; private set; } |
| 49 | public override bool HasCraftButton |
| 61 | public bool ReadyToStart |
| 80 | public IEnumerable<HumanItemData> PartyPreview |
| 95 | public Dungeon() |
| 113 | public override void Start() |
| 121 | public void SetDungeonType(DungeonType dt) |
| 155 | public override void UpdateUpgrades() |
| 172 | public override bool CanManualCraft() |
| 181 | public override void Update(float delta) |
| 207 | public void CheckForParty(bool manual) |
| 234 | public override void DoManualCraft() |
| 239 | public override bool HandleReopenBuyMenu() |
| 245 | protected override void CopySettingsTo(FlowElement copy) |
| 253 | protected override void DataToJson(JsonObject data) |
| 261 | protected override void DataFromJson(JsonObject data, FlowDiagram parent) |

## Documented by

| Wiki article |
| --- |
| [Dungeon](building-Dungeon.md) |
| [Dungeon runs, stages, loot, and retreat](dungeon-run-mechanics.md) |

## Sources

- `Assets.Source.Flow.Elements/Dungeon.cs:1`
