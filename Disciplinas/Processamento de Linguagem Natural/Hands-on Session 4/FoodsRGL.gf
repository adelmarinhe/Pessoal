abstract FoodsRGL =
FoodsRGLLexicon **
{
flags startcat = Phrase ;
cat
Phrase ; Item ; Kind ; Quality ;
fun
Is : Item -> Quality -> Phrase ;
NIs : Item -> Quality -> Phrase ;

This, That : Kind -> Item ;
These, Those : Kind -> Item ;

N2Kind : N -> Kind ;
QKind : Quality -> Kind -> Kind ;

A2Quality : A -> Quality ;
Very : Quality -> Quality ;
}