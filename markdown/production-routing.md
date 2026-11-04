# Collectors, Distributors, and Manifolds

Different merging and splitting tools have different priority behavior.

## Collector

Collector begins with two inputs and one output, each buffered for one item. If the output has room, it tries the current input; after a transfer or an empty attempt it advances to the next connected input.

It skips disconnected inputs when advancing, but tries only the selected input in a single update. An empty selected input therefore costs an update before another input is tried. Additional inputs can be added; collapse removes only disconnected trailing slots while keeping at least two.

## Distributor

Distributor begins with one input and two outputs. It sends one item to the current output and advances to the next connected output. If the selected output is full, it advances and returns for that update.

Distributor skips disconnected outputs when advancing, but does not inspect the downstream item's filter before placing an item into an output buffer. An incompatible item can thus occupy that branch and stall it. Additional outputs are supported; collapse retains at least two.

## Manifold

Manifold has matching numbers of inputs and outputs, starting at two each. It scans inputs from the first slot and outputs from the first slot, sending one waiting item to the first connected output with buffer space, then returns.

Unlike the rotating Collector and Distributor, this is fixed input and output priority. A continuously supplied early input can take precedence over later inputs. Downstream compatibility is handled by pipes after the transfer, so filters still matter.

## Sources

- `Assets.Source.Flow.Elements/Collector.cs:88`
- `Assets.Source.Flow.Elements/Collector.cs:107`
- `Assets.Source.Flow.Elements/Distributor.cs:95`
- `Assets.Source.Flow.Elements/Distributor.cs:112`
- `Assets.Source.Flow.Elements/Manifold.cs:90`
