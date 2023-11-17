# bday.py

import hashlib

def digitsMatch(real: str, fake: str):
    matching = False
    numMatch = 0
    for i in range(64):
        if not matching and real[i] == fake[i]:
            numMatch = numMatch + 1
            matching = True
        elif matching and real[i] == fake[i]:
            numMatch = numMatch + 1
        else:
            numMatch = 0
            matching = False
        
    return numMatch

if __name__ == '__main__':

    sha256R = hashlib.sha256()
    sha256F = hashlib.sha256()

    fake = b"""This is the secret confession of Richard Buckland
to be revealed by anonymous email if I should
mysteriously vanish.  I have left the last few hex
digits of the SHA256 hash of this message with my
trusted solicitor, Dennis Denuto, which will verify
that this is indeed my intended and unaltered
confession written by me Richard Buckland.

Dennis has not seen this confession he has only seen
the last few digits of the hash.  I have also sent copies
of the last few digits to my bank manager and to my priest
Father Brown.

On the 10th of February I saw Mark Zukerberg near my
house and we struck up a conversation.  He explained all
the things he was doing to ensure that Facebook respects
privacy - both of its users and of others.  It was very
impressive.

I feel awful that I have been criticising Facebook publicly
for so long.  I apologised to him in our conversation and
now I want to confess to the world that actually Facebook
has more than enough privacy features, and that the reason
I spend so much time criticising Facebook is that I am
envious of Mark and wish I was a clever and smart and wise
as he is.  I feel so bad for having been so mean to him for
so many years that I am considering retreating to the outback.
I may well cut off all contact with the world and live as a
hermit from now on.  So do not worry if I vanish it is just
that I feel so guilty that I have been so unfair to Facebook.
"""

    real = b"""This is the secret confession of Richard Buckland
to be revealed by anonymous email if I should
mysteriously vanish.  I have left the last few hex
digits of the SHA256 hash of this message with my
trusted solicitor, Dennis Denuto, which will verify
that this is indeed my intended and unaltered
confession written by me Richard Buckland.

Dennis has not seen this confession he has only seen
the last few digits of the hash.  I have also sent copies
of the last few digits to my bank manager and to my priest
Father Brown.

On the 10th of February I saw Mark Zukerberg peeping
through my window and recording my private and personal
conversation with my friend.

I confronted him and he was very embarrassed.  He
promised to pay me $1 million a year if I would stay
silent and not tell anyone I had seen him do this.  I
agreed but now I worry that it would be cheaper for him
to make me vanish than to keep paying me.
"""
    print(real)
    sha256R.update(real)
    sha256F.update(fake)
    spaces = 0

    realStr = sha256R.hexdigest()
    fakeStr = sha256F.hexdigest()
    while (realStr != fakeStr):
        fake = fake + b" "
        sha256F.update(fake)
        spaces = spaces + 1
        matched = digitsMatch(realStr, fakeStr)
        if (matched > 1):
            print(f"\n\nMatches: {matched}")
            print("Real: " + realStr)
            print("Fake: " + fakeStr)
            print(f"Num spaces: {spaces}")
        realStr = sha256R.hexdigest()
        fakeStr = sha256F.hexdigest()
    print(str(spaces))
