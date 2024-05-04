# alice-and-bob-py

Adapted from Luca Dellanna's [.NET repo](https://github.com/lucadellanna/Alice-and-Bob)

## How to Run Locally

- Install Python 3.11 (probably works on other versions, but untested)
- Optional: Create virtualenv
- `python main.py`
- Tweak input params in main.py (note, if you set them high the calcs will take a long time to run) and rerun to explore


## Commentary

This code demonstrates the importance of survivorship bias.

From [_Winning Long Term Games_](https://luca-dellanna.com/winning-long-term-games/) (pp.43-44):

> Imagine two entrepreneurs, Alice and Bob. They each open a busi- ness with an initial capital of $100,000. Alice takes more risks and, as a result, has a high growth rate of 10%. However, because of those risks, she also has a high failure rate of 5%. Conversely, Bob takes less risks. As a result, his growth rate is lower, 8%, but so is his failure rate, 1%.
> Who do we expect to make the most money: Alice or Bob?
> The answer is counterintuitive: Alice is more likely to be wealthier
> than Bob, yet we expect Bob to end up wealthier.
> Let me explain.
> If we consider periods of a single year, Alice is expected to be wealthier than Bob 95% of the time. Yet, if you compare the expected wealth, Alice’s is 95% times $100,000 times 110% = $104,500, whereas Bob’s is 99% times $100,000 times 108% = $106,920. Bob’s expected wealth is higher than Alice’s despite him being less likely to be wealthier than her.
> Here is another way to see it. Given a hundred Alices and a hundred Bobs, the top 95 wealthiest entrepreneurs would all be Alices. Yet, on aggregate, Bobs would have more wealth.
> Survivorship bias makes us think that Alice’s strategy is better because all the winners are Alices, but her strategy is not better. Alice’s strategy has higher potential but is less reproducible; there- fore, she ends up worse, at the net of survivorship bias.

RUNNING A SIMULATION
I ran a Monte Carlo simulation, computing the results of ten million Alices and ten million Bobs running their businesses for ten years (using the same parameters as the previous example).
The results of the simulation are telling.
The top 10% of entrepreneurs by wealth are all Alices! That gives the impression that Alice’s strategy is worth imitating more than Bob’s.
And yet, the average Alice has only $155,000, whereas the average Bob has $195,000. Bob ends up 26% wealthier despite not appearing in the top decile even once!
What’s even more surprising is that, if we only consider the surviving Alices (i.e., those who didn’t fail), their average wealth is a whopping $259,000, whereas the wealth of the average surviving Bob is only $195,000. However, we shouldn’t look at only the surviving Alices – we should look at all of them.
This experiment shows how misleading survivorship bias is.
The strategy producing the most winners is not always the best strategy for you.


You see this in the code output for simulation 2:

```markdown
Iteration 20:
% Alices in top 10: 100.0%
% Alices in top 100: 100.0%
% Alices in top decile: 100.0%
Surviving Alices' avg: 673.0
Surviving Bobs' avg: 466.0
Alices' avg: 240.0
Bobs' avg: 381.0
```

Despite Alice dominating, the **average** Bob is doing a lot better.