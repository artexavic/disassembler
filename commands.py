commands = """1001010kkkkk110kkkkkkkkkkkkkkkkk-jmp k
1001000ddddd0000kkkkkkkkkkkkkkkk-lds Rd,k
1001001rrrrr0000kkkkkkkkkkkkkkkk-sts k,Rr
1001010kkkkk111kkkkkkkkkkkkkkkkk-call k
0110KKKKddddKKKK-sbr Rd,K
0111KKKKddddKKKK-cbr Rd,K
000011rdddddrrrr-add Rd,Rr
000111rdddddrrrr-adc Rd,Rr
10010110KKddKKKK-adiw Rdl,K
000110rdddddrrrr-sub Rd,Rr
0101KKKKddddKKKK-subi Rd,K
000010rdddddrrrr-sbc Rd,Rr
0100KKKKddddKKKK-sbci Rd,K
10010111KKddKKKK-sbiw Rdl,K
001000rdddddrrrr-and Rd,Rr
0111KKKKddddKKKK-andi Rd,K
001010rdddddrrrr-or Rd,Rr
0110KKKKddddKKKK-ori Rd,K
001001rdddddrrrr-eor Rd,Rr
1001010ddddd0000-com Rd
1001010ddddd0001-neg Rd
1001010ddddd0011-inc Rd
1001010ddddd1010-dec Rd
11101111dddd1111-ser Rd
100111rdddddrrrr-mul Rd,Rr
00000010ddddrrrr-muls Rd,Rr
000000110ddd0rrr-mulsu Rd,Rr
000000110ddd1rrr-fmul Rd,Rr
000000111ddd0rrr-fmuls Rd,Rr
000000111ddd1rrr-fmulsu Rd,Rr
1100kkkkkkkkkkkk-rjmp k
1001010000001001-ijmp
1001010000011001-eijmp
1101kkkkkkkkkkkk-rcall k
1001010100001001-icall
1001010100011001-eicall
1001010100001000-ret
1001010100011000-reti
000100rdddddrrrr-cpse Rd,Rr
000101rdddddrrrr-cp Rd,Rr
000001rdddddrrrr-cpc Rd,Rr
0011KKKKddddKKKK-cpi Rd,K
1111110rrrrr0bbb-sbrc Rr,b
1111111rrrrr0bbb-sbrs Rr,b
10011001PPPPPbbb-sbic P,b
10011011PPPPPbbb-sbis P,b
111100kkkkkkksss-brbs s,k
111101kkkkkkksss-brbc s,k
111100kkkkkkk000-brcs k
111101kkkkkkk000-brcc k
111100kkkkkkk000-brlo k
111101kkkkkkk000-brsh k
111100kkkkkkk001-breq k
111101kkkkkkk001-brne k
111100kkkkkkk010-brmi k
111101kkkkkkk010-brpl k
111100kkkkkkk011-brvs k
111101kkkkkkk011-brvc k
111100kkkkkkk100-brlt k
111101kkkkkkk100-brge k
111100kkkkkkk101-brhs k
111101kkkkkkk101-brhc k
111100kkkkkkk110-brts k
111101kkkkkkk110-brtc k
111100kkkkkkk111-brie k
111101kkkkkkk111-brid k
1110KKKKddddKKKK-ldi Rd,K
001011rdddddrrrr-mov Rd,Rr
00000001ddddrrrr-movw Rd,Rr
1001000ddddd1100-ld Rd,X
1001000ddddd1101-ld Rd,X+
1001000ddddd1110-ld Rd,-X
1000000ddddd1000-ld Rd,Y
1001000ddddd1001-ld Rd,Y+
1001000ddddd1010-ld Rd,-Y
10q0qq0ddddd1qqq-ldd Rd,Y+q
1000000ddddd0000-ld Rd,Z
1001000ddddd0001-ld Rd,Z+
1001000ddddd0010-ld Rd,-Z
10q0qq0ddddd0qqq-ldd Rd,Z+q
1001001rrrrr1100-st X,Rr
1001001rrrrr1101-st X+,Rr
1001001rrrrr1110-st -X,Rr
1000001rrrrr1000-st Y,Rr
1001001rrrrr1001-st Y+,Rr
1001001rrrrr1010-st -Y,Rr
10q0qq1rrrrr1qqq-std Y+q,Rr
1000001rrrrr0000-st Z,Rr
1001001rrrrr0001-st Z+,Rr
1001001rrrrr0010-st -Z,Rr
10q0qq1rrrrr0qqq-std Z+q,Rr
1001010111001000-lpm
1001000ddddd0100-lpm Rd,Z
1001000ddddd0101-lpm Rd,Z+
1001010111011000-elpm
1001000ddddd0110-elpm Rd,Z
1001000ddddd0111-elpm Rd,Z+
1001010111101000-spm
1001010111111000-spm Z+
10110PPdddddPPPP-in Rd,P
10111PPrrrrrPPPP-out P,Rr
1001001rrrrr1111-push Rr
1001000ddddd1111-pop Rd
10011010PPPPPbbb-sbi P,b
10011000PPPPPbbb-cbi P,b
1001010ddddd0110-lsr Rd
1001010ddddd0111-ror Rd
1001010ddddd0101-asr Rd
1001010ddddd0010-swap Rd
1111101rrrrr0bbb-bst Rr,b
1111100ddddd0bbb-bld Rd,b
100101000sss1000-bset s
100101001sss1000-bclr s
1001010000001000-sec
1001010010001000-clc
1001010000011000-sez
1001010010011000-clz
1001010000101000-sen
1001010010101000-cln
1001010000111000-sev
1001010010111000-clv
1001010001001000-ses
1001010011001000-cls
1001010001011000-seh
1001010011011000-clh
1001010001101000-set
1001010011101000-clt
1001010001111000-sei
1001010011111000-cli
0000000000000000-nop
1001010110001000-sleep
1001010110101000-wdr
1001010110011000-break"""