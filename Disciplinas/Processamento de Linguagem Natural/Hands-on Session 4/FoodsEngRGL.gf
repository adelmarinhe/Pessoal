concrete FoodsEngRGL of FoodsRGL =
FoodsEngRGLLexicon **
open
SyntaxEng,
StructuralEng
in {
lincat
Phrase = Phr ;
Item = NP ;
Kind = CN ;
Quality = AP ;
lin
Is item quality = mkPhr (mkCl item quality) ;
NIs item quality =
mkPhr (mkS negativePol (mkCl item quality)) ;

This kind = mkNP (mkDet this_Quant singularNum) kind ;
That kind = mkNP (mkDet that_Quant singularNum) kind ;
These kind = mkNP (mkDet this_Quant pluralNum) kind ;
Those kind = mkNP (mkDet that_Quant pluralNum) kind ;

N2Kind n = mkCN (lin N n) ;
QKind quality kind = mkCN quality kind ;

A2Quality a = mkAP (lin A a) ;
Very quality = mkAP very_AdA quality ;
}