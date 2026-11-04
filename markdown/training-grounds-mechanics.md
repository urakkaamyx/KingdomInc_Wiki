# Training Grounds and quality growth

Sessions, dummies, food, repeat energy costs, and specialization timing.

## Session

A session has 10 training ticks, normally every 2 ÷ Speed seconds. A manual action independently has a 50% chance to tick each occupied slot. The Capacity property starts at 3 and rises to 5 with research; intake scans the full five-slot array, so the property alone does not establish an enforced cap.

Each tick requests quality gain of QualityPerTick × building quality, affected by training traits, then awards a random half-to-full share. QualityPerTick is 0.02 without a dummy, 0.04 with one.

Ordinary humans get full gain in their first session, half in their second, and zero from the third onward. Adventurers retain full gain. A nonhuman dummy takes trainee base damage ÷ 10 on ticks with positive gain multiplier; dead dummies are removed.

## Energy and food

Each tick costs 2 × (1 + TrainingCount) Energy before traits. With food research and Food equipped this is halved; automatic training also performs a second tick for food-bearing trainees each cycle. Food is consumed at completion while that technology is active.

At halfway, specialization research checks advancement if the energy payment did not exhaust the trainee. Exhausted trainees are removed. Finished trainees wait for output space, receive ActivityCompleted, and increase TrainingCount (ordinary humans stop incrementing at 3).

## War cleanup

War Effort separately cleans non-adventurer humans with TrainingCount above 4: the count becomes 4 and quality is capped at 1.5. This differs from ordinary training diminishing returns.

## Sources

- `Assets.Source.Flow.Elements/TrainingGrounds.cs:39`
- `Assets.Source.Flow.Elements/TrainingGrounds.cs:71`
- `Assets.Source.Flow.Elements/TrainingGrounds.cs:151`
- `Assets.Source.Flow.Elements/TrainingGroundsSlot.cs:41`
- `Assets.Source.Items.Data/CombatantItemData.cs:340`
- `Assets.Source.Flow.Elements/WarEffort.cs:113`
