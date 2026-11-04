# GamePlayer — source reference

Assets.Source.Player/GamePlayer.cs · 1,004 lines · 18 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 17 | public class GamePlayer |
| 19 | public static GamePlayer Current |
| 21 | public readonly List<FlowDiagram> Flows = new List<FlowDiagram>() |
| 43 | public readonly HashSet<string> UnlockedDungeons = new HashSet<string>() |
| 53 | public readonly Dictionary<TechNode, int> NewTechCount = new Dictionary<TechNode, int>() |
| 55 | public Vector2Int TechTreeCamera |
| 57 | public int TechTreeZoom = 3 |
| 59 | public int FlowZoom |
| 61 | public int CurrentFlow |
| 63 | public List<ItemType> RequisitionTypes = new List<ItemType>() |
| 65 | public int GameTime |
| 67 | public Register Register = new Register() |
| 69 | public int AscensionCount |
| 71 | public int NightmareCount |
| 73 | public int NightmareCountActive |
| 75 | public float NightmareProgress = 1f |
| 77 | public bool NightmareActive = true |
| 87 | public ForestSettings ForestSettings |
| 89 | public FarmSettings FarmSettings |
| 91 | public readonly ArmoryContents Armory = new ArmoryContents() |
| 93 | public readonly PortalContents Portal = new PortalContents() |
| 95 | public FlowDiagram ActiveFlow => Flows[CurrentFlow] |
| 97 | public Vector2Int FlowCamera |
| 105 | public IEnumerable<WarProgress> Wars => _warProgress.Values |
| 107 | public int NightmareAvailable |
| 124 | public GamePlayer() |
| 133 | public void Start() |
| 141 | public void Update(float delta) |
| 169 | public CurrencyCollection GetCurrencies() |
| 174 | public long GetCurrency(Currency c) |
| 179 | public void AddCurrency(Currency c, long amt, bool isIncome) |
| 193 | public void AddCurrency(CurrencyCollection currency, bool isIncome) |
| 201 | public bool SpendCurrency(Currency c, long amt) |
| 211 | public bool SpendCurrency(CurrencyCollection cost) |
| 224 | public bool CanAfford(CurrencyCollection cost) |
| 236 | public bool CanAfford(Currency c, long amt) |
| 241 | public bool HasTech(TechNode tech) |
| 250 | public void AddTech(TechNode tech, bool notify = false) |
| 323 | public void AddResource(ResourceItemType resource, double amt, bool isUpgrade = false) |
| 333 | public void SetFarmResource(FarmItemType item, double amt) |
| 369 | public double GetResourceAvailable(ResourceItemType resource) |
| 374 | public double GetResourceDemand(ResourceItemType resource) |
| 385 | public float GetResourceQuotaMultiplier(ResourceItemType resource) |
| 390 | public float GetResourceOutput(ResourceElement res) |
| 395 | public IEnumerable<(ResourceItemType resource, double quota)> GetAvailableResources() |
| 410 | public (double quota, CurrencyCollection cost) GetResourceUpgrade(ResourceItemType resource) |
| 422 | public double GetResourceCostMultiplier(ResourceItemType resource) |
| 432 | public int GetElementCount(FlowElement type) |
| 449 | internal IEnumerable<T> GetElements<T>() where T : FlowElement |
| 463 | public int GetUpgradeSlotCount(string elementType) |
| 469 | public void SetUpgradeSlotCount(string elementType, int count) |
| 474 | public void AddAvailableFlowUpgrade(string elementType, string upgradeType) |
| 484 | public IEnumerable<string> GetAvailableFlowUpgrades(string elementType) |
| 508 | public void UnlockWar(WarType warType) |
| 513 | public void UpdateWarProgress() |
| 521 | public WarProgress GetWarProgress(WarType warType) |
| 527 | public WarProgress GetWarProgress(WarStage stage) |
| 542 | public bool HasWarStage(WarType type, int stage) |
| 547 | public bool HasWarStage(WarStage stage) |
| 562 | public QuestMetadata GetQuestMetadata(Quest quest) |
| 573 | public DungeonProgress GetDungeonProgress(DungeonType dt) |
| 593 | public DungeonMetadata GetDungeonMetadata(DungeonType dungeon) |
| 604 | public void UnlockDungeon(DungeonType dt) |
| 609 | public List<Armory> GetArmoryList(int channel, ItemType itemType) |
| 626 | public List<Portal> GetPortalList(int channel, int channelIndex) |
| 639 | public CurrencyCollection GetExtraWorkflowCost() |
| 654 | public float GetExchangeTax(Currency currency) |
| 665 | public int GetPrestigePoints(PrestigeNode node) |
| 670 | public void SetPrestigePoints(PrestigeNode node, int count) |
| 675 | public void DoAscension() |
| 701 | public JsonValue ToJson() |
| 847 | public static GamePlayer FromJson(JsonValue json) |
| 985 | public static GamePlayer CreateNewPlayer() |

## Documented by

| Wiki article |
| --- |
| [All Nodes](achievement-AllNodes.md) |
| [All Recipes](achievement-AllRecipes.md) |
| [All Tech](achievement-AllTech.md) |
| [Gold Earned1](achievement-GoldEarned1.md) |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Ascension and what carries over](ascension.md) |
| [Building, copying, and area movement](building-and-blueprints.md) |
| [Currencies and currency exchange](currencies-and-exchange.md) |
| [Prestige perks and refunds](prestige-perks.md) |
| [Currencies and the exchange](production-currency-exchange.md) |
| [Mines and supply depots](production-mines-suppliers.md) |
| [Resource quotas and harvesting](production-resources.md) |
| [Production simulation and bottlenecks](production-simulation.md) |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |
| [Saves, autosaves, pause, and offline behavior](saves-time-and-offline.md) |
| [Starting a kingdom](starting-a-kingdom.md) |
| [Technology requirements and unlocking](technology-rules.md) |
| [War Effort combat, medals, and defense](war-effort-mechanics.md) |

## Sources

- `Assets.Source.Player/GamePlayer.cs:1`
