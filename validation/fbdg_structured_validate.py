from itertools import product
import random

# Points: 1=U0, 2=U1, 3=L1, 4=U2, 5=L2, 6=R1, 7=R2
LINES = {
    '123': (1,2,3),
    '145': (1,4,5),
    '167': (1,6,7),
    '246': (2,4,6),
    '257': (2,5,7),
    '347': (3,4,7),
    '356': (3,5,6),
}
ASSIGN = {'123':(0,1),'145':(0,2),'167':(0,1),'246':(1,2),'257':(0,1),'347':(0,2),'356':(0,1)}
PAIR_LINES = {
    (0,1): ['123','167','257','356'], # all omit U2=4
    (0,2): ['145','167','347','356'], # all omit U1=2
    (1,2): ['246','257','347','356'], # all omit U0=1
}

def encode_copy(x):
    # x indexed 1..7
    c0=(x[1],x[3],x[5])
    c1=(x[2],x[6],x[7])
    c2=(x[4],x[3]^x[6],x[5]^x[7])
    return c0,c1,c2

def decode_all(pair, c0,c1,c2):
    c=[c0,c1,c2]
    a,b=pair
    # reconstruct all points except the Ui omitted by this pair
    if pair==(0,1):
        return {1:c0[0],3:c0[1],5:c0[2],2:c1[0],6:c1[1],7:c1[2]}
    if pair==(0,2):
        return {1:c0[0],3:c0[1],5:c0[2],4:c2[0],6:c2[1]^c0[1],7:c2[2]^c0[2]}
    if pair==(1,2):
        return {2:c1[0],6:c1[1],7:c1[2],4:c2[0],3:c2[1]^c1[1],5:c2[2]^c1[2]}
    raise ValueError(pair)

def check_fano_exhaustive():
    cases=0
    assigned_cases=0
    for bits in product([0,1], repeat=7):
        x={i+1:bits[i] for i in range(7)}
        c0,c1,c2=encode_copy(x)
        for name,pair in ASSIGN.items():
            dec=decode_all(pair,c0,c1,c2)
            assert all(dec[p]==x[p] for p in LINES[name])
            assigned_cases += 1
        for pair, names in PAIR_LINES.items():
            dec=decode_all(pair,c0,c1,c2)
            for name in names:
                assert all(dec[p]==x[p] for p in LINES[name])
                cases += 1
    return assigned_cases, cases

def query_patterns(t):
    # Three fixed patterns ensure every source point in every copy is active.
    patterns=[]
    patterns.append(((0,2), tuple(['145']*t)))
    patterns.append(((1,2), tuple(['246']*t)))
    patterns.append(((0,2), tuple(['347']*t)))
    needed=7*t-len(patterns)
    for seq in product(PAIR_LINES[(0,1)], repeat=t):
        patterns.append(((0,1), seq))
        needed -= 1
        if needed==0:
            break
    assert len(patterns)==7*t
    assert len(set(patterns))==7*t
    return patterns

def encode_t(state,t):
    # state[(copy, point)]
    words=[[],[],[]]
    for r in range(t):
        x={p:state[(r,p)] for p in range(1,8)}
        cs=encode_copy(x)
        for k in range(3):
            words[k].append(cs[k])
    return words

def check_t(t, trials=1000, seed=1):
    pats=query_patterns(t)
    # active coverage
    active=set()
    for pair,seq in pats:
        for r,name in enumerate(seq):
            for p in LINES[name]: active.add((r,p))
    assert len(active)==7*t
    rng=random.Random(seed+t)
    for _ in range(trials):
        state={(r,p):rng.randrange(2) for r in range(t) for p in range(1,8)}
        words=encode_t(state,t)
        for pair,seq in pats:
            a,b=pair
            for r,name in enumerate(seq):
                c0,c1,c2=(words[0][r],words[1][r],words[2][r])
                dec=decode_all(pair,c0,c1,c2)
                assert all(dec[p]==state[(r,p)] for p in LINES[name])
    return len(pats), len(active), trials*len(pats)

if __name__=='__main__':
    assigned, allvalid=check_fano_exhaustive()
    print('Fano fixed-assignment exhaustive state/query cases:', assigned)
    print('Fano all-valid-pair exhaustive cases:', allvalid)
    for t in [1,2,3,4,5,8]:
        if t==1:
            # the generic 7t selector above requires 4^t >= 7t-3 and works here too (4 >=4)
            pass
        print('t=',t, 'result=',check_t(t, trials=200 if t>=5 else 1000))
