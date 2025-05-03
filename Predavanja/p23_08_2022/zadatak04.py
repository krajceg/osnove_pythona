from viberUser import ViberUser
from viberMessage import ViberMessage
from viberReaction import ViberReaction

sender1 = ViberUser("Sinan", "Sakic", 62444555, False)
receiver1 = ViberUser("Mitar", "Miric", 63777999, False)
reaction1 = ViberReaction("smile", receiver1)

message1 = ViberMessage("What's up?", sender1, receiver1)
message1.set_reaction(reaction1)

message1.show_message()
