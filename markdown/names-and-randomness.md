# Character names and random generation

Stable seeded names, six cultures, surname patterns, and live versus deterministic rolls.

## Stable names

HumanDetailsPopup creates a random stream from the human item GetSeed() plus NameGen, then generates and displays FullName. The same seed with the same generator implementation produces the same name when reopened. This is derived presentation rather than a separate stored rename system.

## Culture selection

| Culture | Weight and chance | Given syllables |
| --- | --- | --- |
| Northmark | 45 / 100 = 45% | 2–3 |
| Veyran | 15 / 100 = 15% | 2–4 |
| Sarenic | 12 / 100 = 12% | 2–3 |
| Ashan | 10 / 100 = 10% | 2–3 |
| Vaelic | 10 / 100 = 10% | 2–4 |
| Orsian | 8 / 100 = 8% | 2–3 |

## Assembly

Given names combine a weighted start, random syllable count, weighted middles and ending. Weighted surname patterns include compound, root/suffix, prefix, patronymic, place, two-part and fixed pool; cultures use their own subsets. Cleaning collapses selected repeated vowels/consonants and capitalizes space/hyphen-separated parts.

WeightedList sums max(1,weight), samples an integer below the total, and chooses the cumulative matching entry. Empty lists throw. Culture selection uses the same minimum-one weight rule.

## Seeds and distributions

SeedGenerator hashes ASCII string bytes through a 64-bit xor/multiply FNV-style hash with separator bytes. JSON object keys are sorted; array order is retained. SeededRandom advances and mixes a 64-bit state. Integer ranges are lower-inclusive, upper-exclusive; RandomFloat is in [0,1). RandomGaussian uses a Box–Muller-style transform; RandomScatter uses standard deviation baseVal×scatter/2. Item seeds contain eight alphanumeric characters.

## Reproducibility limits

Research prices use a fresh stream seeded by identifier. Human names use item seed plus NameGen. Live choices may use Global, seeded from DateTime.Now.Ticks for the process. The inspected player save does not serialize Global’s state; a stable item seed does not make every global future roll replayable.

## Sources

- `Assets.Behaviour.UI.Human/HumanDetailsPopup.cs:109`
- `Assets.Source.Name/HumanNameGenerator.cs:46`
- `Assets.Source.Name/HumanNameGenerator.cs:83`
- `Assets.Source.Name/HumanNameGenerator.cs:126`
- `Assets.Source.Name/HumanNameGenerator.cs:203`
- `Assets.Source.Name/HumanNameGenerator.cs:319`
- `Assets.Source.Name/WeightedList.cs:21`
- `SeedGenerator.cs:20`
- `SeededRandom.cs:19`
- `SeededRandom.cs:41`
- `SeededRandom.cs:65`
