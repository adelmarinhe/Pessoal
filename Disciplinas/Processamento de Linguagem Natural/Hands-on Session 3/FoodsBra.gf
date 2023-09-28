concrete FoodsBra of Foods = open Prelude in {
param
Number = Sg | Pl ;

lincat
Phrase = SS ;
Quality = {s : Number => Str} ;
Kind = {s : Number => Str} ;
Item = {s : Str ; n : Number} ;
oper
det : Number -> Str -> {s : Number => Str} -> {s : Str ; n : Number} =
\n,d,cn -> {
s = d ++ cn.s ! n ;
n = n
} ;

noun : Str -> Str -> {s : Number => Str} =
\man,men -> {s = table { Sg => man ; Pl => men } } ;

regNoun : Str -> {s : Number => Str} =
\car -> noun car (car + "s") ; -- Pluralize nouns simply by adding "s"


regAdj : Str -> {s : Number => Str} =
      \adj -> noun adj (adj + "s") ;  -- Pluralize adjectives simply by adding "s"


copula : Number -> Str =
\n -> case n of { Sg => "é" ; Pl => "são" } ;

lin
Is item quality = ss (item.s ++ copula item.n ++ quality.s ! item.n) ;

This = det Sg "este" ;
That = det Sg "aquele" ;
These = det Pl "estes" ;
Those = det Pl "aqueles" ;
QKind quality kind = {s = table {n => quality.s ! n ++ kind.s ! n}} ;
Wine = regNoun "vinho" ;
Cheese = regNoun "queijo" ;
Fish = regNoun "peixe" ;
Very quality = {s = table {n => "muito" ++ quality.s ! n}} ;
Fresh = regAdj "fresco" ;
Warm = regAdj "morno" ;
Italian = regAdj "Italiano" ;
Expensive = regAdj "caro" ;
Delicious = regAdj "delicioso" ;
Boring = regAdj "tedioso" ;
}