abstract Foods = {
flags
startcat = Phrase ;
cat
Phrase ; Item ; Kind ; Quality ;
fun
Is : Item -> Quality -> Phrase ;
This, That : Kind -> Item ;
These, Those : Kind -> Item ;
QKind : Quality -> Kind -> Kind ;
Wine, Cheese, Fish : Kind ;
Very : Quality -> Quality ;
Fresh, Warm, Italian, Expensive : Quality ;
Delicious, Boring : Quality ;
}