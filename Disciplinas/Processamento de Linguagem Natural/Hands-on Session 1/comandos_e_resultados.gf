module name FoodEng differs from file name FoodBR

Languages: FoodEng
0 msec
Food> q
See you.
0 msec
PS C:\Users\jams\Documents\Pessoal\Disciplinas\Processamento de Linguagem Natural> gf

         *  *  *
      *           *
    *               *
   *
   *
   *        * * * * * *
   *        *         *
    *       * * * *  *
      *     *      *
         *  *  *

This is GF version 3.10.
Built on mingw32/x86_64 with ghc-8.4, flags: interrupt server
License: see help -license.


Languages:
> import FoodEng.gf FoodBR.gf
- compiling FoodBR.gf...   write file FoodBR.gfo
linking ... OK

Languages: FoodBR FoodEng
0 msec
Food> generate_random -number=5 -tr | linearizeIs (This (QKind (Very Italian) Wine)) DeliciousIs (This (QKind Fresh Wine)) Fresh
Is (That (QKind Boring Wine)) Italian
Is (This Cheese) Delicious
Is (This (QKind Italian Cheese)) Italian

este vinho muito Italiano é delicioso
this very Italian wine is delicious
este vinho fresco é fresco
this fresh wine is fresh
aquele vinho tedioso é Italiano
that boring wine is Italian
este queijo é delicioso
this cheese is delicious
este queijo Italiano é Italiano
this Italian cheese is Italian

0 msec
                                              n0 msec
Food> generate_random -number=5 -tr | linearize -lang=FoodBR
Is (That Fish) Warm
Is (This (QKind Boring Fish)) Italian
Is (That (QKind (Very Expensive) (QKind Italian Wine))) Delicious
Is (That Cheese) Italian
Is (This Cheese) Expensive

aquele peixe é morno
este peixe tedioso é Italiano
aquele vinho Italiano muito caro é delicioso
aquele queijo é Italiano
este queijo é caro

0 msec
Food>