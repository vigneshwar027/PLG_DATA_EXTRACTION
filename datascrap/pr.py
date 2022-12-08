from string import ascii_letters

a = '''$99
$850 +$15 Control and authentication
$357
$55
$350
$320$279
$359$339 +$15 Control and authentication
$90
$300
$63
$361$250
$366
$48
$310
$130
$357
$369$329 +$15 Control and authentication
$342$290
$361$290
$154
$50
$48
$29
$83
$500
$38
$361 +$15 Control and authentication
$174
$244 +$15 Control and authentication
$30
$450$400
$1,400 +$15 Control and authentication
$120
$25
$80
$80
$80
$100$85
$149
$200
$80
$143
$100
$112
$1,250 +$15 Control and authentication
$175
$670
$200
$750
$140
$78
$60
$425
$2,000 +$15 Control and authentication
$380
$75
$58
$75
$361
$269
$29
$1,200 +$15 Control and authentication
$285
$320
$52
$285
$31
$450
$395
$77
$244
$200
$192
$250
$653 +$15 Control and authentication
$333
$333
$250
$320
$20
$1,600 +$15 Control and authentication
$130
$20
$25
$73
$450
$1,800 +$15 Control and authentication
$380
$40
$950
$19
$580 +$15 Control and authentication
$199
$18
$187
$800
$800
$180
$750$600
$240
$600$400
$145$116
$199
$599
$499
$90
$43
$90
$225
$225
$534
$800
$372
$180
$400
$600
$70
$100
$496
$452
$71
$315
$80
$40
$40
$358
$168
$445
$320
$260
$1,500 +$15 Control and authentication
$379
$379
$80
$60
$454
$189
$108
$80
$439
$139
$290
$350
$350
$800
$1,400 +$15 Control and authentication
$1,400 +$15 Control and authentication
$40
$1,600 +$15 Control and authentication
$485
$460
$385
$490$320
$400
$475
$548
$100
$390$290
$175
$275
$685
$59
$38
$419
$419
$398
$224
$359
$135
$369
$465$425
$500
$36
$26
$200
$419
$215
$294
$395
$22
$22
$22
$23
$375$349
$169
$518 +$15 Control and authentication
$275
$300
$395
$395
$30
$50
$78
$379
$366$209
$398
$180
$398
$388
$450
$295
$442
$368
$299
$335
$288
$150
$800
$475
$133
$357
$285
$385
$398
$379
$419
$249
$375$359
$475
$203
$369
$398
$398
$400
$203
$250
$334
$333
$335
$305
$375$345
$379
$305
$379
$379
$200
$369
$390$250
$195
$450$415
$590$360
$419
$390$389
$419
$313
$398
$200$177
$439
$398
$571
$566
$275
$285$270
$325
$59
$395
$173
$295
$175
$395
$288
$425
$195
$375
$324
$250
$450
$345 +$15 Control and authentication
$450
$475
$455
$285$232
$425
$425
$200
$325
$450
$150
$395
$455
$395
$399
$249
$750
$267
$425
$120
$120
$395
$225
$120
$395
$395
$460 +$15 Control and authentication
$285
$90
$376
$500
$495 +$15 Control and authentication
$445
$450
$575
$285
$339
$120
$425
$90
$395
$395
$484
$487
$395
$340
$484
$484
$484
$134
$419
$375$359
$475$349
$475
$545$525
$120$116
$750
$54
$520
$375
$518 +$15 Control and authentication
$333
$275
$398
$50
$359
$583
$398
$389$365
$280
$280
$280
$280
$280
$484
$399
$392.51$360
$299$269
$455
$334
$325$280
$100
$415
$224
$445
$257
$334
$375 +$15 Control and authentication
$325$280
$365
$350$290
$315
$360
$390
$499
$200
$124$114
$484
$484
$484
$484
$280
$341
$175
$35
$295
$495$420
$1,000 +$15 Control and authentication
$312$270 +$15 Control and authentication
$334
$334
$459 +$15 Control and authentication
$350
$349
$199
$209$150
$359 +$15 Control and authentication
$484
$350
$225
$280
$225
$267$227
$313
$225
$895 +$15 Control and authentication
$200
$341
$360
$323
$323
$320
$359$305
$89$74.34
$425
$370$369
$459
$475 +$15 Control and authentication
$350
$399
$81
$350$265
$360$359
$180
$535
$280
$348
$238
$1,300 +$15 Control and authentication
$462
$222
$395
$350
$425
$375
$200
$250
$225
$990 +$15 Control and authentication
$799$550
$225
$225
$265 +$15 Control and authentication
$375$349
$490$290
$499
$895 +$15 Control and authentication
$400
$485
$500
$349$325
$188
$350 +$15 Control and authentication
$175
$478
$295
$447
$150
$390$305
$800$700
$180
$355
$200
$350
$499
$487
$439
$447
$584
$375$349
$375$349
$525
$575
$380
$295$280
$205
$499$425
$132
$429 +$15 Control and authentication
$274
$319
$419
$353$300
$300
$198
$395 +$15 Control and authentication
$210
$419
$250
$350
$470
$425$395 +$15 Control and authentication
$795 +$15 Control and authentication
$150
$459 +$15 Control and authentication
$400
$187
$546
$508
$315
$400
$200
$287
$245
$300
$120$110
$326
$385
$535
$999$800 +$15 Control and authentication
$470
$295
$450$425 +$15 Control and authentication
$154
$1,196$1,181
$350
$125$75
$389
$615$495
$380$350
$161$145
$375
$400
$260$180
$494
$499
$419
$337
$561
$465$345
$575$549
$580$499
$565$495
$350$340 +$15 Control and authentication
$65
$315
$172
$299
$350
$200
$389$349
$575$549
$300$275
$200
$38
$265
$150
$299
$398
$200
$309
$250
$545$449
$210
$499$149
$399
$167
$300
$499 +$15 Control and authentication
$379$359
$244
$455$349
$200 +$15 Control and authentication
$289$205
$150
$309$297
$235$175
$200
$176
$379$365
$1,121 +$15 Control and authentication
$535$455
$565$525
$385$345
$589
$702 +$15 Control and authentication
$425$382
$399$359
$400$179
$135
$898
$640
$190
$200
$35
$385$359
$175
$565
$299
$287
$127$125
$349$325
$535$455
$400$321
$340
$430$389
$324
$334
$314
$334
$300
$775$699
$150
$70$63
$371
$371
$225
$225
$225
$299
$250
$425$375
$419
$419
$419
$250
$323
$379$360
$650 +$15 Control and authentication
$980 +$15 Control and authentication
$200
$398
$200
$295
$350
$300
$135
$315
$459
$459
$419
$225
$433$415
$338
$459
$371
$695
$371
$250
$340
$360
$278
$320
$459
$318
$364
$500 +$15 Control and authentication
$425
$120$118
$399
$522
$425
$225
$337
$337
$117
$175
$371
$520
$2,900$375
$396
$38
$419
$459 +$15 Control and authentication
$120
$120
$568
$384
$225
$409
$330
$200
$100
$260
$220
$45
$419
$419
$398
$1,250 +$15 Control and authentication
$230
$1,800 +$15 Control and authentication
$498
$520
$513
$450
$398
$320$319 +$15 Control and authentication
$459
$169
$369
$100
$350
$420
$348
$285$275 +$15 Control and authentication
$710 +$15 Control and authentication
$136$129
$575
$300
$280
$240
$250$180
$239
$349
$515
$225
$399
$200
$200
$350
$333
$225
$580
$245
$651 +$15 Control and authentication
$279$269
$584
$199
$18
$238
$299
$450
$280
$475
$371
$220
$1,580$1,350 +$15 Control and authentication
$459
$459
$459
$280$263
$500$404
$25
$24
$289
$200
$350$310
$325 +$15 Control and authentication
$475 +$15 Control and authentication
$399
$350
$150
$200
$350
$350
$289
$350
$315$305
$315
$350
$387
$399
$275
$333
$70
$375
$895 +$15 Control and authentication
$375 +$15 Control and authentication
$485
$485
$485
$485
$315
$350
$550 +$15 Control and authentication
$405 +$15 Control and authentication
$419
$184
$300 +$15 Control and authentication
$280$279
$235
$40
$44
$460 +$15 Control and authentication
$298
$250
$26
$293
$125$113
$175$170
$250$248
$250$247
$566 +$15 Control and authentication
$850 +$15 Control and authentication
$383
$410 +$15 Control and authentication
$75
$330
$30
$225
$459
$760 +$15 Control and authentication
$480 +$15 Control and authentication
$460 +$15 Control and authentication
$39
$500$250 +$15 Control and authentication
$180
$296
$135
$371
$300$280
$300
$480 +$15 Control and authentication
$300
$204
$320
$475 +$15 Control and authentication
$795 +$15 Control and authentication
$35
$300
$200
$240
$207
$419
$239
$300
$399
$475
$195
$450 +$15 Control and authentication
$238
$240$220
$90
$450
$319
$319
$649 +$15 Control and authentication
$435 +$15 Control and authentication
$440 +$15 Control and authentication
$163
$341
$269
$440 +$15 Control and authentication
$352
$569
$475 +$15 Control and authentication
$370 +$15 Control and authentication
$410 +$15 Control and authentication
$447 +$15 Control and authentication
$410 +$15 Control and authentication
$180
$239
$225
$594 +$15 Control and authentication
$275
$210$198
$960$845
$199
$375
$400
$425
$399
$495 +$15 Control and authentication
$59
$41
$498
$480
$579
$150
$120
$26$20
$26
$99$75
$1,196$1,181
$38
$326
$420
$289
$100
$250
$480 +$15 Control and authentication
$150
$425 +$15 Control and authentication
$425 +$15 Control and authentication
$250
$400$370
$399
$399
$399
$70
$299
$390$350
$1,500$1,000 +$15 Control and authentication
$395
$400$375
$288
$771 +$15 Control and authentication
$110
$350$300
$342$338
$29
$429$385
$300
$269
$469
$200$189
$519
$63
$508
$520
$135
$400$129
$771 +$15 Control and authentication
$771 +$15 Control and authentication
$400
$349
$500 +$15 Control and authentication
$1,196$1,181
$771 +$15 Control and authentication
$25
$399
$350
$350
$400
$390
$341
$489
$341
$380
$249$205
$300
$325
$595 +$15 Control and authentication
$319 +$15 Control and authentication
$490$390
$167
$595 +$15 Control and authentication
$515
$489
$314
$891
$250
$200
$140
$150
$120
$112$84
$341
$326
$375
$371
$357
$359
$359
$313 +$15 Control and authentication
$370
$400
$250
$569
$395$295
$360
$225
$561
$1,012 +$15 Control and authentication
$35
$290$247
$99$75
$329
$200
$400
$550
$200
$470 +$15 Control and authentication
$350
$450$424 +$15 Control and authentication
$385
$250$200
$595 +$15 Control and authentication
$595 +$15 Control and authentication
$595 +$15 Control and authentication
$470 +$15 Control and authentication
$399
$520
$595 +$15 Control and authentication
$469 +$15 Control and authentication
$200 +$15 Control and authentication
$199
$285
$345
$200
$200
$200
$349$314
$220 +$15 Control and authentication
$495
$275$199
$365
$560 +$15 Control and authentication
$318
$475
$475
$185
$480$434
$463$425
$380
$2,000$888 +$15 Control and authentication
$1,094 +$15 Control and authentication
$469 +$15 Control and authentication
$352
$284
$237
$591
$220 +$15 Control and authentication
$335
$290$247
$184$173
$165$150
$165$150
$463
$268
$170
$420
$375
$64$48
$150
$695$591
$561
$489$474
$499
$399$359
$350
$584
$1,700 +$15 Control and authentication
$220 +$15 Control and authentication
$175
$185
$184
$652
$337$323
$44
$184
$188
$220
$80
$171
$175$117
$380
$330
$330
$159
$417
$420
$63
$51
$20
$97
$339
$398
$250$106
$357
$298
$170$112
$315
$330
$216
$216
$129
$375
$510
$595 +$15 Control and authentication
$70
$285
$216
$40
$40
$285
$216
$595
$216
$269
$216
$470 +$15 Control and authentication
$250
$1,380 +$15 Control and authentication
$342$220
$324$316
$480
$330
$487
$579
$499
$75
$350$298
$545$409
$685 +$15 Control and authentication
$324
$656
$250
$324$316
$250
$184
$184
$225
$148$130
$350
$335
$300
$590$399
$319
$750
$300
$366
$357
$487
$190
$800
$315
$410$349
$366
$250
$112$89
$200
$272$204
$250
$595$575
$435$415
$280
$350$315
$180
$595
$352
$333
$341
$154
$250
$349
$323
$308
$308
$290
$469 +$15 Control and authentication
$371
$250
$330
$315
$341
$325
$325
$200$179
$499
$400
$119
$308
$350 +$15 Control and authentication
$58
$1,295$995
$50$38
$62$47
$438
$470 +$15 Control and authentication
$280
$183
$550$475
$150$100
$100
$1,100$1,000 +$15 Control and authentication
$100
$480
$748$500
$364
$420$335
$590
$400
$450$350
$32
$300
$450
$1,011 +$15 Control and authentication
$220
$300$280
$590
$27
$55
$515
$341
$345
$376
$424 +$15 Control and authentication
$630 +$15 Control and authentication
$279
$360
$653 +$15 Control and authentication
$200
$498
$498
$227
$500$400 +$15 Control and authentication
$55
$20
$162.33 +$15 Control and authentication
$450
$225
$520$450 +$15 Control and authentication
$425
$150
$190
$38
$704$572
$400
$595 +$15 Control and authentication
$653 +$15 Control and authentication
$44
$200
$320
$325
$565$424 +$15 Control and authentication
$535$401 +$15 Control and authentication
$199
$170
$120$107
$400
$120
$350
$236
$210
$44
$44
$653 +$15 Control and authentication
$275$200
$490$295
$40
$400
$325
$167
$50
$53
$72
$100$77
$298
$320
$500
$450
$28
$44
$75
$297$281
$500$415
$180
$299
$485
$350$279
$389$306
$183
$1,100$1,000 +$15 Control and authentication
$200$130 +$15 Control and authentication
$280
$184
Sold at $400 on November 21, 2022
$665$473 +$15 Control and authentication
$450
$44
$299
$175
$450
$315
$695$591
$210
$299
$199
$387
$342
$299
$599$499 +$15 Control and authentication
$250
$1,938
$399
$250
$159
$390
$350
$225
$344
$379
$159.08 +$15 Control and authentication
$175$157
$709 +$15 Control and authentication
$538
$269
$280
$899
$65
$290
$239
$249
$280
$350$298
$44
$44
$400
$20
$348
$872$749
$1,099 +$15 Control and authentication
$1,093$920
$200
$805
$920
$300
$239
$260$246
$155$117
$310
$310
$949
$300
$388$350
$500
$1,040
$215
$265
$261
$351
$715
$124
$27
$29
$390
$185
$250
$250
$99$58
$180
$455
$179
$220
$250
$250
$250
$300
$212
$674$549
$329
$420
$190
$159$120
$284
$375
$480
$360
$480
$261
$140
$379$315
$45$40
$450
$261
$310
$88
$185
$50
$425$410
$35
$270
$125
$250
$266
$250
$212
$352
$185
$185
$225
$550
$317
$369
$150
$275$181
$358
$52
$330$193
$490$417
$689
$290$261
$266
$949
$370
$240
$261
$250$150
$191
$695$509
$230
$1,175$985
$425$352
$380
$342
$200
$255$254
$249
$280
$40
$618$577
$475$338
$180
$200
$385
$385
$165$124
$390
$399
$180
$35
$361.63 +$15 Control and authentication
$490$353
$270
$400
$399
$337
$275$265
$170$125
$399
$46
$399$299
$573
$490$260
$385$335
$320
$173
$450
$195
$225
$60
$120
$272$263
$736 +$15 Control and authentication
$88
$280
$1,095$1,065 +$15 Control and authentication
$298
$60$43
$140$130
$398
$398
$335$330 +$15 Control and authentication
$178$97
$175
$124
$355$251
$345
$285
$600$500
$90
$189
$500$350
$220
$438
$108
$575
$176
$295
$40$23
$180$141
$25
$220
$225
$520
$330
$295$148
$210
$210
$300
$297
$295
$292
$295
$199
$450$415
$150
$310
$310
$310
$310
$334
$115
$180
$250$200
$375
$835
$381
$1,560 +$15 Control and authentication
$900
$235$215
$455$323
$395
$1,350$1,215 +$15 Control and authentication
$20
$750
$199
$68.18 +$15 Control and authentication
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$1,500 +$15 Control and authentication
$230
$225$185
$225$185
$410$409
$300
$475
$2,091
$98
$361$345
$40
$125$115
$300
$154$148
$190
$125
$630
$300
$270
$200$180
$288$279
$195
$295$275
$129
$28
$1,195 +$15 Control and authentication
$325
$325
$325
$325
$175
$49
$80$65
$172$164
$212.47 +$15 Control and authentication
$399
$272$263
$389$388
$368
$725 +$15 Control and authentication
$340
$474
$400
$554
$365
$695$521
$520
$95
$345
$345
$395$299
$559
$188$96
$35
$350$250
$266
$103.89 +$15 Control and authentication
$149
$50
$550
$130
$489$474
$618 +$15 Control and authentication
$795$520
$38$29
$150
$449
$255
$280
$170
$309
$600
$155
$1,380 +$15 Control and authentication
$320
$320
$225
$800$750
$530 +$15 Control and authentication
$185
$225
$325$300
$350
$290
$899
$275
$358
$358 +$15 Control and authentication
$460
$260
$200
$70
$38
$317
$275$240
$110
$355
$85
$399
$200
$805
$175
$260
$329
$329
$320
$279$189
$483
$83
$160
$310$300
$289
$450$275
$293$278
$279
$420
$300
$183
$920
$595
$590$290
$310
$310
$27
$465
$130$81
$350
$836$795
$335$320
$175
$355
$213
$400$370
$580
$350
$210
$389
$124
$325
$200
$200
$289
$439$402
$285
$225
$225
$345
$1,552 +$15 Control and authentication
$450
$352
$1,560 +$15 Control and authentication
$289
$1,284 +$15 Control and authentication
$581$538
$200
$250$240
$398
$288
$229
$298$289
$195
$345
$345
$345
$415
$550
$280
$350
$295
$295
$429$375
$80
$44
$628
$1,093 +$15 Control and authentication
$395
$435
$200
$109
$236
$199
$295$275
$320
$1,035 +$15 Control and authentication
$55
$438
$544
$305
$520
$80$52
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$395
$398
$398
$324
$280
$370$369
$385$349
$335$320
$500$450
$229
$202
$420
$32
$290$238
$280$279
$130$120
$324
$1,300$1,267 +$15 Control and authentication
$158
$25
$350$310
$500$448 +$15 Control and authentication
$56.82$44.32 +$15 Control and authentication
$1,000 +$15 Control and authentication
$150$119
$200
$600
$289$288
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$300$245
$525
$348$333
$310
$180$148
$575
$236
$249
$320
$559$399
$355$315
$500
$310
$179
$310
$300$299
$350
$415
$395
$374$356
$382
$280
$320
$439
$129
$325
$350
$700$400
$420
$248
$120
$150$98
$325
$325
$325
$325
$325
$325
$325
$325
$180
$351$298
$799 +$15 Control and authentication
$1,200 +$15 Control and authentication
$225$185
$400
$520
$190
$317$301
$139
$527
$280
$550
$108
$44
$270
$537
$361$345
$361$345
$46
$200
$292
$499$349
$480
$329
$681$525
$398
$559
$559
$225
$329
$487
$349
$675$504
$1,247$1,238 +$15 Control and authentication
$200
$475$430
$320
$27
$305
$329
$169
$225$180
$179$146
$270$225
$195
$250
$550
$550
$736 +$15 Control and authentication
$345
$230
$350
$69
$207$191
$460
$395
$300
$209$171
$1,035 +$15 Control and authentication
$648
$250
$250
$475$435
$315
$230
$1,399 +$15 Control and authentication
$200$170
$399
$1,035 +$15 Control and authentication
$500$401
$245
$280
$60
$648
$288$279
$220$190
$300$269
$435$420
$850
$850
$115
$898$888 +$15 Control and authentication
$499
$255
$650$400
$1,284 +$15 Control and authentication
$375
$300$299
$275
$310
$552 +$15 Control and authentication
$398$370 +$15 Control and authentication
$35$32
$95
$275
$375
$335
$335
$335
$476
$290$274
$325
$344
$350
$750 +$15 Control and authentication
$467
$322$307
$295
$231
$289$288
$695
$500$400
$420
$600$316
$19
$185
$593
$360
$230
$348
$330
$547
$275$230
$335
$136.36$122.72
$285
$469
$209
$370
$23
$108
$275
$199$120
$250
$2,200 +$15 Control and authentication
$295
$2,162
$108
$350
$65
$220
$27
$60
$325
$560
$1,483 +$15 Control and authentication
$300
$354$353
$335
$320
$339
$345
$345
$345
$345
$345
$345
$345
$345
$345
$345
$350
$285
$995$314 +$15 Control and authentication
$360
$115$105
$35
$30
$375
$348
$614
$140$119
$345
$65
$298
$425
$350
$45
$250$195
$425$410
$361$345
$1,560 +$15 Control and authentication
$350
$920
$635
$249
$361$345
$361$345
$350
$350
$350
$299$250
$89
$300$269
$130
$225$185
$479
$98$89
$1,750 +$15 Control and authentication
$348
$488
$487
$200
$86
$106
$429$378
$255$247
$320
$121
$215$185
$649
$512
$138
$300
$170
$115$89
$1,725 +$15 Control and authentication
$450
$190$127
$80
$345
$1,035 +$15 Control and authentication
$550$315
$89
$89$76
$265$235
$525
$330
$330
$300
$1,250 +$15 Control and authentication
$299
$119
$298
$185
$284.08$244.30 +$15 Control and authentication
$176
$348
$348
$350
$2,000 +$15 Control and authentication
$80
$239
$375
$230
$265
$310
$400$221 +$15 Control and authentication
$600 +$15 Control and authentication
$398
$320
$450$435
$295
$400
$400
$186$181
$533
$492
$405
$75
$39
$65
$470
$555
$32
$275
$480$448
$228
$420
$420
$390
$552 +$15 Control and authentication
$485
$335
$65
$475
$1,076 +$15 Control and authentication
$400
$350
$282
$36
$420
$598 +$15 Control and authentication
$230
$393.16
$310
$339
$84
$200
$275
$64
$220
$310
$400
$295
$550
$216$214
$495
$600$560
$338$330
$200
$455
$995$775
$200
$850
$27
$252
$365
$60
$185
$600
$238
$280
$600$588
$398
$462
$210
$398
$83
$301
$669$349
$335
$261
$261
$26
$1,200 +$15 Control and authentication
$133
$226$165
$600$465
$300
$287$216
$74
$470
$398
$398
$398
$409
$36
$345
$450$419
$295
$590
$253
$102
$285
$271
$811
$310
$200
$194$173
$398
$431
$199
$3,795 +$15 Control and authentication
$275
$480$425
$1,035 +$15 Control and authentication
$735
$285
$1,035 +$15 Control and authentication
$258
$3,995$3,550 +$15 Control and authentication
$452
$250
$750$690
$890$634
$344
$81
$248
$420
$300
$419
$145
$625$469
$546$505
$420
$250
$400$390
$552 +$15 Control and authentication
$273
$399$329
$255
$350
$350
$200
$230
$350
$412$398
$489$279
$811
$1,093 +$15 Control and authentication
$442 +$15 Control and authentication
$800$788
$492 +$15 Control and authentication
$330
$283
$476$427
$1,250 +$15 Control and authentication
$1,984$1,850 +$15 Control and authentication
$295
$375
$420
$199
$785
$693
$728$429
$174
$179
$649
$32
$1,799 +$15 Control and authentication
$162$122
$185
$250
$473
$460
$250
$360
$260
$263
$370
$990$705
$199$185
$925$626
$184
$155
$299
$25
$180$153
$460
$451
$175
$549
$233$232
$215
$125
$455
$175$149
$40
$269
$215
$799$599
$455
$225
$190$169
$270
$300
$650$468
$315
$495
$1,800$1,700 +$15 Control and authentication
$464
$716$489
$215
$192
$350
$200
$43
$375
$176
$258
$260
$475
$132
$442
$596
$1,250$950
$250
$254
$1,100 +$15 Control and authentication
$315$305
$21
$980
$35$32
$465
$160
$489
$265
$520$484 +$15 Control and authentication
$440
$320
$320
$435$405 +$15 Control and authentication
$451
$295
$185
$461$452
$823
$299
$215$213
$313
$649
$320
$310
$305
$300
$187$159
$280
$549
$300$225
$694
$371
$370
$300
$1,700$1,688 +$15 Control and authentication
$489
$865$649
$403$395
$171$128
$1,059$924
$1,036$1,024 +$15 Control and authentication
$1,036$1,024 +$15 Control and authentication
$1,036$1,024 +$15 Control and authentication
$1,036$1,024 +$15 Control and authentication
$1,036$1,024 +$15 Control and authentication
$474
$718
$580
$284
$795$447
$238
$255
$242
$660
$350
$297
$100
$100
$100
$100
$372
$285
$285
$285
$285
$285
$285
$285
$240
$596
$920$776
$300
$1,150 +$15 Control and authentication
$285
$375
$356
$345
$353
$1,476 +$15 Control and authentication
$255$224
$320
$373
$120
$870$809 +$15 Control and authentication
$283
$102
$110
$110
$1,036$1,024 +$15 Control and authentication
$360
$95
$300
$760
$710
$310
$640$595 +$15 Control and authentication
$400
$120
$250
$273
$356
$250
$258
$560$521 +$15 Control and authentication
$242
$520
$360
$370
$280$234
$469 +$15 Control and authentication
$432
$20
$480
$245
$245
$649
$295
$500
$652
$40
$425$400
$1,128
$1,128
$240
$227
$1,036$1,024 +$15 Control and authentication
$1,250$1,240 +$15 Control and authentication
$1,750 +$15 Control and authentication
$438
$538
$311
$330
$295
$295
$295
$295
$295
$295
$295
$295
$295
$400
$250
$258
$425
$1,036$1,024 +$15 Control and authentication
$1,036$1,024 +$15 Control and authentication
$1,036$1,024 +$15 Control and authentication
$284
$55$50
$288
$284
$363
$363
$119
$295
$35
$77
$295$269
$400
$240
$325
$40
$250
$100
$350
$652
$240
$333
$285$265
$240
$430
$77
$31
$295
$225$165
$333
$480$415
$625
$985$700
$240
$258
$450
$489
$335
$1,563$1,551 +$15 Control and authentication
$950$500
$480
$480
$100$90
$345
$258
$475
$20
$300
$260
$370
$84
$265
$305
$305
$305
$400$276
$305
$305
$305
$305
$305
$305
$305
$245
Sold at $150 on November 17, 2022
$400
$375
$93
$518
$500$218
$82
$58
$199$168
$499$450
$1,247$1,234 +$15 Control and authentication
$455
$201
$1,195$1,194 +$15 Control and authentication
$329
$400
$1,000$875
$410
$110
$345
$280
$600
$200$189
$110
$180
$360
$41
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$310
$300
$300
$345
$455
$478 +$15 Control and authentication
$475$375
$225
$1,988 +$15 Control and authentication
$120
$469
$910$585
$459
$340
$150
$179
$205
$736
$1,035 +$15 Control and authentication
$575
$400
$96
$865$804 +$15 Control and authentication
$198
$147
$143$125
$85$68
$1,295 +$15 Control and authentication
$261
$110
$300
$250
$100
$394 +$15 Control and authentication
$460
$253
$180
$233$153
$388
$395$355
$180
$180
$180
$265
$365$300
$474
$439
$104
$300
$300
$110
$160
$370
$40
$681
$298
$1,228 +$15 Control and authentication
$382
$589 +$15 Control and authentication
$75
$518
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$320
$462
$315
$518
$518
$299
$1,100$800
$420
$172
$319
$260
$479
$380$275 +$15 Control and authentication
$480$415 +$15 Control and authentication
$284 +$15 Control and authentication
$180 +$15 Control and authentication
$320 +$15 Control and authentication
$360 +$15 Control and authentication
$322$307 +$15 Control and authentication
$335 +$15 Control and authentication
$350 +$15 Control and authentication
$234 +$15 Control and authentication
$240 +$15 Control and authentication
$373 +$15 Control and authentication
$325 +$15 Control and authentication
$297 +$15 Control and authentication
$485 +$15 Control and authentication
$320 +$15 Control and authentication
$310 +$15 Control and authentication
$310 +$15 Control and authentication
$310 +$15 Control and authentication
$320 +$15 Control and authentication
$320 +$15 Control and authentication
$310 +$15 Control and authentication
$300 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$325 +$15 Control and authentication
$450 +$15 Control and authentication
$538 +$15 Control and authentication
$450 +$15 Control and authentication
$1,000 +$15 Control and authentication
$38$28 +$15 Control and authentication
$225 +$15 Control and authentication
$590 +$15 Control and authentication
$390 +$15 Control and authentication
$295 +$15 Control and authentication
$40 +$15 Control and authentication
$75 +$15 Control and authentication
$185$165 +$15 Control and authentication
$230 +$15 Control and authentication
$575$499 +$15 Control and authentication
$376 +$15 Control and authentication
$760 +$15 Control and authentication
$35 +$15 Control and authentication
$250 +$15 Control and authentication
$530 +$15 Control and authentication
$196 +$15 Control and authentication
$463 +$15 Control and authentication
$235 +$15 Control and authentication
$316 +$15 Control and authentication
$375 +$15 Control and authentication
$385 +$15 Control and authentication
$65$53 +$15 Control and authentication
$189$84 +$15 Control and authentication
$988 +$15 Control and authentication
$395 +$15 Control and authentication
$365 +$15 Control and authentication
$350$320 +$15 Control and authentication
$695 +$15 Control and authentication
$310 +$15 Control and authentication
$310 +$15 Control and authentication
$310 +$15 Control and authentication
$424 +$15 Control and authentication
$931$918 +$15 Control and authentication
$220 +$15 Control and authentication
$105 +$15 Control and authentication
$105 +$15 Control and authentication
$105 +$15 Control and authentication
$285 +$15 Control and authentication
$550 +$15 Control and authentication
$180 +$15 Control and authentication
$55 +$15 Control and authentication
$250 +$15 Control and authentication
$235 +$15 Control and authentication
$288$260 +$15 Control and authentication
$30 +$15 Control and authentication
$35 +$15 Control and authentication
$410 +$15 Control and authentication
$250$235 +$15 Control and authentication
$168$148 +$15 Control and authentication
$273 +$15 Control and authentication
$208$206 +$15 Control and authentication
$260$239 +$15 Control and authentication
$66$50
$100
$90
$7,647 +$15 Control and authentication
$250$198
$280
$230
$325$250
$30
$360
$145
$335
$1,699 +$15 Control and authentication
$250
$567
$398
$1,329 +$15 Control and authentication
$194
$200
$660$640
$450
$430$400
$863
$570$498
$235
$110
$538
$590
$350
$400
$770
$480
$140$125
$599$529
$518
$770
$50
$289$185
$399
$1,036$1,024 +$15 Control and authentication
$500
$413$410
$295
$550$385
$565
$249
$320
$266
$365$345
$308$268
$450
$275$259
$400$300
$325
$470
$359
$200
$249$225
$273
$273
$155
$382
$450
$450
$450
$345
$345
$345
$345
$345
$345
$345
$345
$345
$345
$345
$345
$345
$345
$800
$185
$700
$900
$490$400
$400
$159
$360
$1,144$1,073 +$15 Control and authentication
$158
$594
$594
$593
$800
$305
$4,200 +$15 Control and authentication
$170
$1,900 +$15 Control and authentication
$128
$431
$585$499
$78
$730
$1,045$1,040 +$15 Control and authentication
$270
$175
$929
$68
$39$34
$395
$283
$475
$550
$520
$229$190
$310
$310
$310
$310
$6,900 +$15 Control and authentication
$250
$60
$300
$229$190
$355
$125
$585
$215
$540$394
$310
$100$90
$525
$600$378
$350$250
$585
$348
$839$680
$473
$847
$250
$56
$589
$39$35
$470
$348$280
$249
$431
$295
$721$709
$721$709
$583
$59
$59
$110
$110
$144
$229
$489
$1,698$1,688 +$15 Control and authentication
$477
$150
$2,299$2,288 +$15 Control and authentication
$800$788
$537
$485$388
$250$200
$228
$35
$229$195
$75
$450
$289
$459
$400
$700$420
$320
$296
$320
$320
$168.96
$310
$39$34
$150
$290
$396
$96
$199
$500$350
$474
$530
$249
$175
$650$550
$595
$160
$209
$460
$32
$325
$325
$325
$310
$375$356
$115
$285$265
$1,563$1,550 +$15 Control and authentication
$349
$550
$379
$250
$499$424
$368
$495$460
$380
$380
$1,970 +$15 Control and authentication
$30$24
$265
$240$225
$379$365
$530
$40
$310
$310
$295$221
$320
$1,030$958 +$15 Control and authentication
$325
$550
$258$229
$250
$159
$800
$384
$275
$1,563$1,552 +$15 Control and authentication
$1,563$1,551 +$15 Control and authentication
$65
$125
$320
$400
$400
$114
$375
$353
$420 +$15 Control and authentication
$207$204
$335
$388
$389
$237
$190
$1,762 +$15 Control and authentication
$285
$660$640
$260
$385
$285
$168.96$139.67
$600$400
$315$237
$150$140
$978
$575$550
$617
$280
$283
$1,434 +$15 Control and authentication
$389
$615$603
$480
$615$603
$615$602
$182
$425
$1,228 +$15 Control and authentication
$690
$189
$230
$460
$75
$360
$395
$350$197
$395$249
$540
$238
$188
$350
$466
$52
$68
$18
$575 +$15 Control and authentication
$575 +$15 Control and authentication
$555$390 +$15 Control and authentication
$388
$295
$66$50
$389
$130
$335
$1,128
$345
$40
$800
$349
$390$315
$431
$350$299
$334
$300
$466
$404
$290 +$15 Control and authentication
$350
$800$650
$374
$615$603
$399
$39$34
$695
$470$446
$30$26
$120
$1,036$1,024 +$15 Control and authentication
$350
$399
$240$164
$345
$30$24
$32$26
$590
$590
$590
$503
$590
$590
$193
$615$602
$500$488
$700$688
$615$603
$700$459
$699
$386
$319
$319
$385
$350
$355
$556
$388
$403
$150
$590
$503
$26
$431
$1,247$1,235 +$15 Control and authentication
$120
$264
$275$265
$132.92
$475
$1,900 +$15 Control and authentication
$1,247$1,234 +$15 Control and authentication
$449
$459
$20
$20
$20
$20
$20
$350$254
$30
$590
$590
$590
$590
$590
$570 +$15 Control and authentication
$89
$1,233 +$15 Control and authentication
$108
$350$349
$149
$695
$95
$1,195 +$15 Control and authentication
$1,345 +$15 Control and authentication
$375$359
$493
$57
$400
$180
$375
$375
$375
$375
$375
$375
$291$252
$380$320
$370
$330
$285
$650
$950$884 +$15 Control and authentication
$428$353
$448
$325
$425$375
$300
$145
$338
$376.10 +$15 Control and authentication
$695
$350$299
$405
$2,475 +$15 Control and authentication
$550
$600
$360
$445
$142$127
$616
$80
$150
$590
$1,780 +$15 Control and authentication
$468
$400$380
$300
$40
$396
$650$499
$120
$185
$969$800
$1,236 +$15 Control and authentication
$43
$339
$75
$260$179
$39$35
$283
$289
$26
$335
$250
$408
$99
$2,800 +$15 Control and authentication
$184
$574
$275
$180
$590
Sold at $1,000 on November 18, 2022
$20
$268$252
$500
$178$133
$265
$88$66
$240 +$15 Control and authentication
$498
$500
$499$424
$300
$403
$365$330
$350$220
$400
$395$375
$599
$145
$842$830
$153
$359
$50
$604
$490
$215
$550
$485$368
$355
$300
$42$32
$1,563$1,551 +$15 Control and authentication
$250$162
$84
$85
$70
$395
$350
$340
$500
$550
$220
$250
$288
$403
$299
$795
$59
$1,500 +$15 Control and authentication
$842
$675
$475
$20
$20
$650$565
$183$177
$419
$503
$503
$503
$503
$503
$503
$503
$699
$595
$550
$45$43.01
$168
$350
$430
$75
$387
$275
$129$89
$503
$503
$360
$370
$1,499 +$15 Control and authentication
$360
$560$100
$360
$503
$258
$208
$1,250 +$15 Control and authentication
$299$212
$590$500
$180$120
$503
$75$65
$280
$305
$210
$220
$1,062$1,060
$100$90
$503
$503
$503
$400$388
$407
$328$265
$71
$180$115
$188
$403
$415$311
$200
$183
$499$449 +$15 Control and authentication
$248
$180
$573
$380$230
$30
$61
$132
$20
$30
$20
$20
$30
$20
$379
$265
$140
$175
$552
$389
$195
$225
$380$316
$597
$240$235
$183
$325$292
$35
$350
$500$481
$1,183
$721$709
$250
$695
$1,485 +$15 Control and authentication
$100$90
$187
$51
$100
$167
$42
$49
$403
$2,500 +$15 Control and authentication
$350
$350
$600$588
$721$707
$325
$6,785 +$15 Control and authentication
$400
$425
$70
$530
$899
$95
$315.39$295.12 +$15 Control and authentication
$83
$108.80
$375
$325
$75$16
$359
$430
$180
$495
$2,615$2,603 +$15 Control and authentication
$135
$304
$2,800 +$15 Control and authentication
$525
$2,362 +$15 Control and authentication
$465
$154
$230$200
$200
$495$425
$395$379
$550
$185$120
$584.64$479.40 +$15 Control and authentication
$580
$1,900$1,425
$600
$425
$390
$37$28
$20
$230$229
$425
$188
$1,999 +$15 Control and authentication
$325$165
$79
$240
$385$274
$83
$72
$745.41
$74
$256$208
$599$549
$103$93
$444$333
$500$485
$467.71$444.32
$256
$484$450
$243
$1,000$875
$98.84
$87
$96
$350
$25
$1,563$1,551 +$15 Control and authentication
$159$128
$367
$688
$150
$60
$200
$1,200 +$15 Control and authentication
$300
$440$409
$115
$356$189
$284
$60
$151
$250$128
$1,792 +$15 Control and authentication
$425
$325
$182
$575
$620$577
$43
$420
$20
$125
$100
$100
$185$114
$160
$200
$65
$120
$265
$79
$149$111
$358
$473
$240
$279
$1,247$1,234 +$15 Control and authentication
$78
$500$425 +$15 Control and authentication
$117
$345
$470
$283
$366
$55
$899$599
$63.64
$358
$102$77
$4,200$3,770 +$15 Control and authentication
$350
$74
$235
$250
$280
$570$500
$500$449 +$15 Control and authentication
$500$449 +$15 Control and authentication
$243
$658
$171
$245
$999
$142$127
$300$290
$95
$416
$84$59
$45
$110
$250
$1,800$772.16
$230
$473
$375
$649
$425
$556
$348
$392
$380
$398
$388
$388
$448
$395
$399
$355
$399
$375
$355
$388
$388
$427
$441$249
$360$335
$250
$429
$85
$270
$182
$140
$933$921
$40
$385$320
$305
$220
$320
$325
$285
$775$581
$2,721$2,710 +$15 Control and authentication
$387
$370$100
$374
$158
$205
$600$587
$240 +$15 Control and authentication
$365
$445
$300$262
$114$105
$150$110
$81.10
$2,350 +$15 Control and authentication
$20
$510$497
$510$497
$615$603
$554$541
$826$814
$325$250 +$15 Control and authentication
$78
$25
$660
$600
$1,999 +$15 Control and authentication
$350$263
$65
$660$640
$32
$200
$350
$200
$24$22
$250
$270
$77$62
$110
$288$272
$325
$117$88
$803
$170
$100$31
$365
$349
$35
$920
$455
$1,275 +$15 Control and authentication
$400
$215
$420$399
$870$779
$240$193
$1,195 +$15 Control and authentication
$239$200
$249$225
$895$662
$210
$119
$215
$250$249 +$15 Control and authentication
$170
$297
$270
$390$351
$380 +$15 Control and authentication
$55
$63
$465
$350$298
$972
$450
$285$235
$440
$182
$826$812
$384$350
$372$350
$435
$61
$505
$152.06
$375$325
$1,679 +$15 Control and authentication
$466
$945
$220$199
$721$708
$615$603
$826$814
$54
$1,400 +$15 Control and authentication
$460
$372$276
$826$813
$182
$495
$826$812
$900$570
$354$245
$900$825
$415$311
$190$173
$185
$423$270
$1,093 +$15 Control and authentication
$600
$485
$270
$279
$466
$483
$50
$100$90
$108
$88
$57
$883
$240$200
$995 +$15 Control and authentication
$900
$370$350
$450
$230
$699
$130$114
$200
$150$75
$260$245
$98
$249
$1,050$977 +$15 Control and authentication
$199
$199
$100$60
$298
$721$708
$220$198
$106
$580$539
$650
$285
$50
$599$557
$375$249
$312
$385
$399$395
$525
$600$567
$1,325$1,199
$325
$475$319
$185
$480
$850
$260
$425
$154
$118
$79
$740$688
$619
$90$68
$225
$149
$750 +$15 Control and authentication
$599
$66$50
$270
$1,228 +$15 Control and authentication
$210
$400
$499$475
$233$219
$299
$126$125
$618
$2,249$2,248 +$15 Control and authentication
$395$325
$180
$224$219
$204
$440$311
$390
$465
$295$280
$300$280
$299
$295
$418$379
$842
$25
$250
$95$73
$89
$125
$119$110
$720$708
$340
$190
$349
$350
$29
$384
$126$125
$1,095 +$15 Control and authentication
$130$114
$1,020
$535
$450$393
$510$383
$688
$80
$570
$115$109
$154$116
$260$215
$500
$2,499$1,795 +$15 Control and authentication
$1,050$977 +$15 Control and authentication
$400
$1,195 +$15 Control and authentication
$240
$500$495
$280$277
$235
$235
$389.76$354.68
$1,020
$24.78$20.28
$2,999$1,499 +$15 Control and authentication
$95$65
$175
$475
$235$225
$95
$360
$975$838
$96
$600
$265$250
$120
$450$425
$20
$450
$155$140
$155$140
$360
$480$446
$395$285
$49
$272
$388
$400$270
$410$293
$415$296
$465
$1,700 +$15 Control and authentication
$377
$1,200 +$15 Control and authentication
$46$29
$139$131
$585
$475
$257$200
$125
$118$114
$795$725
$368
$420$377
$360.45$289.42
$394
$60$50
$2,628
$200
$490
$61
$466
$400
$399
$2,300$2,280 +$15 Control and authentication
$495
$243
$173$151
$600
$550
$600
$368
$150
$499
$495
$119$110
$132
$131$123
$120
$89
$1,410$1,058
$142$127
$142$127
$872$749
$540$480
$110
$600
$388
$510
$660
$346
$1,400$1,299 +$15 Control and authentication
$300
$450
$249
$40$22
$550$425
$1,500$1,260 +$15 Control and authentication
$295
$94
$445$420
$199
$1,900 +$15 Control and authentication
$427
$95
$260$246
$142$127
$97$73
$450
$215
$187
$230
$595
$100
$250
$154
$425$319
$220
$75
$350
$547
$505$360
$449
$585
$125$88.93
$154
$26$20
$142$127
$155$140
$2,500$1,395 +$15 Control and authentication
$209
$130
$1,150 +$15 Control and authentication
$400
$300$200
$255
$109$82
$431
$416
$368
$399
$100
$590
$60
$294
$100
$440$330
$234$176
$260$240
$75
$66
$120
$1,680 +$15 Control and authentication
$975$749
$350
$495
$230
$99
$619
$619
$1,485$1,195 +$15 Control and authentication
$500
$1,495 +$15 Control and authentication
$200
$399
$475$220
$290
$449
$61
$80
$225
$125$81
$1,400$1,349 +$15 Control and authentication
$595
$505
$498$473
$425$300
$95
$115
$450
$243
$487
$395
$150
$535
$440$311
$535$534
$625$500
$180
$398
$150
$57
$107
$100$90
$485
$152
$400$350
$244
$500$495
$490$368
$490$368
$1,160 +$15 Control and authentication
$552
$539
$599$540
$475$338
$495$475
$90
$350
$375
$1,680 +$15 Control and authentication
$70
$1,495 +$15 Control and authentication
$155$140
$590
$365$286
$420
$964
$120
$200
$490$353
$62$38
$535$401
$535$360
$210$175
$695
$645
$1,130$806
$132$124
$270$233
$380
$569
$1,800 +$15 Control and authentication
$32
$230$228
$84
$99$78
$279
$375
$552
$250
$250
$63.36
$695
$225
$111$102
$34
$380
$1,440 +$15 Control and authentication
$365
$200$153
$230
$325$290
$200
$60
$1,900 +$15 Control and authentication
$810
$300
$535$383
$192
$1,800 +$15 Control and authentication
$295
$545$386
$304
$189
$248$189
$1,599$1,560 +$15 Control and authentication
$387
$495
$480$341
$102
$428
$315
$300
$244
$355$266
$485$345
$108$98
$299
$364
$495
$432
$1,680 +$15 Control and authentication
$633
$633
$633
$157
$634
$410
$475
$1,600$1,480 +$15 Control and authentication
$81
$85
$139$131
$20
$436
$372
$439
$304
$300
$237
$375$359
$340
$455
$455
$217$98
$135
$495$379
$244
$225
$400
$750$649
$70
$374$373
$485$388
$4,900 +$15 Control and authentication
$2,500$1,800 +$15 Control and authentication
$490
$540
$348
$365$218
$1,485 +$15 Control and authentication
$251
$300
$310
$99
$169
$139
$295
$265$246
$20
$119$110
$720
$300$210
$75
$995
$220$218
$960
$470
$90
$888
$105
$395
$626
$110$79
$450
$103$93
$495
$612
$750
$365
$510
$26
$325
$375
$524
$340$316
$42
$610$458
$455
$265
$1,500 +$15 Control and authentication
$795
$1,200 +$15 Control and authentication
$125
$565
$90
$460$425
$740$640
$130
$349
$2,640 +$15 Control and authentication
$1,272 +$15 Control and authentication
$85
$145
$455
$480
$1,700$1,200 +$15 Control and authentication
$55
$255
$612
$700
$39
$90$68
$24
$114$105
$873
$249
$50
$120
$548
$1,320 +$15 Control and authentication
$380$285
$50
$720
$180
$814
$108$98
$235
$358
$358
$2,195 +$15 Control and authentication
$549
$225
$556
$190$135
$1,392 +$15 Control and authentication
$200$170
$515$368
$85.12
$249
$206
$814
$355
$490
$418
$229$99
$499
$68
$63
$211
$350
$171
$500
$495$399
$695
$114$105
$50$47
$368
$563
$294
$455$400
$60
$470$315
$220
$426
$406
$244
$495
$158
$130
$35
$410$293
$345
$475
$125
$200$185
$175
$90
$1,300 +$15 Control and authentication
$1,680 +$15 Control and authentication
$1,872$1,750 +$15 Control and authentication
$391
$50
$265
$264.70 +$15 Control and authentication
$264.70 +$15 Control and authentication
$345
$89
$239
$1,110$863
$495$399
$353
$495$399
$400
$1,095 +$15 Control and authentication
$139$131
$461
$399
$399
$388
$388
$470$353
$790
$495$399
$425
$995
$114$105
$198
$1,195 +$15 Control and authentication
$30
$235
$41$36
$59
$350
$600
$35
$88
$150
$975
$235
$104
$1,475$1,199 +$15 Control and authentication
$614
$21
$435$405
$507$399
$299
$150
$430
$495$429
$520$218
$275$256
$369
$443
$255
$495$429
$35
$325
$215
$400
$425
$132$124
$895
$180
$60
$222$195
$355$335
$500
$495
$600
$300
$90
$2,640 +$15 Control and authentication
$540
$650$620
$572
$585$539
$585$539
$585$539
$150
$499$450
$50
$52
$575$431
$553
$467
$60
$795
$666$650
$72
$415
$95
$549$548
$549$548
$549$548
$549$548
$50
$761$750
$85
$85
$85
$895$795
$1,563 +$15 Control and authentication
$599$583.76
$230$214
$333
$795
$950$920
$67
$495$399
$540$251
$450
$360
$66
$492
$599$557
$99$75
$295$199
$40
$98
$530
$540$405
$349
$545
$265
$120
$384
$295$199
$283
$283
$450
$20
$37
$4,280$2,888
$69$39
$425
$1,500$1,000
$495
$443
$895$865
$425
$513
$200
$415$296
$150
$125
$85
$487
$99
$111
$56
$795
$595
$595
$80
$500
$125
$651
$157
$190
$171
$269
$468
$116
$304
$304
$335$240
$110
$304
$304
$190
$65
$1,395$1,295 +$15 Control and authentication
$495
$379
$379
$340
$325
$395
$302
$302
$1,500 +$15 Control and authentication
$279
$775
$171
$171
$204
$289$288
$125
$160$140
$743
$1,350 +$15 Control and authentication
$35$32
$85$55
$440$285
$1,195$1,095 +$15 Control and authentication
$144
$599
$1,580 +$15 Control and authentication
$792
$495
$492
$176$165
$319$288
$93
$72
$399
$275$256
$495
$38
$495$379
$1,200$650
$80
$70
$129
$438
$315
$1,563 +$15 Control and authentication
$1,188 +$15 Control and authentication
$750
$288$278
$288$278
$1,899 +$15 Control and authentication
$350
$540
$168
$1,288 +$15 Control and authentication
$289$286
$470$437
$500$356
$288$282
$204
$179
$450$400
$495
$731
$495
$1,188 +$15 Control and authentication
$1,125 +$15 Control and authentication
$750
$344
$25
$58
$380
$485
$495
$458$426
$288$282
$680$632
$716
$80
$36
$468
$213$170
$220$218
$1,080
$495
$495
$204
$825
$895
$364
$1,175 +$15 Control and authentication
$279
$279
$237
$237
$237
$468
$269
$269
$269
$995$895
$210$195
$160$94
$443
$279
$279
$310
$200
$279
$716
$279
$279
$430
$661
$661
$110
$110
$799$699
$784$750
$95
$700$685.84
$193
$600$583.99
$154
$667
$650
$350$300
$98
$262
$258
$480
$300$296
$800
$125$100
$257
$240
$322$309
$165$96
$695
$170
$614
$422
$88
$159$120
$895$850
$220$218
$81
$528
$230$229
$230$229
$189$186
$78
$260
$3,336 +$15 Control and authentication
$220$218
$197
$197
$402
$500$450.36
$350
$350
$658
$538
$45
$105
$240
$171
$840
$285
$275
$315
$620$577
$73
$110
$52$45
$365$320
$98$73
$264
$385
$110
$495
$475
$500$430
$950$874.52
$1,119
$399
$450$319
$155
$385$289
$285
$428
$695
$422
$309.76 +$15 Control and authentication
$358$298
$325
$240
$475$356
$184
$36
$150
$100$94.62
$80
$402
$799
$298
$310$288
$1,175 +$15 Control and authentication
$695
$720
$445
$72
$90.11$72.09
$250$150
$284
$295
$95
$508
$424
$200
$175
$630
$175
$95
$480
$40$26
$32
$170
$633
$1,100$858
$45$41.26
$55
$349
$379
$508
$424
$614
$572
$550
$508
$284
$518
$485
$200
$96
$98
$98
$98
$98
$98
$399
$424
$508
$538
$424
$379
$424
$379
$254
$284
$225
$675
$424
$135
$98$73
$424
$650
$125$118
$319$286
$289$286
$85
$213
$27
$195
$174
$118$84
$495$425
$319$296
$243
$145
$492
$950
$85
$144
$650
$102
$220
$499
$198
$400
$405$380
$360
$280
$440
$250
$85
$766$760
$197
$95
$240
$70 +$15 Control and authentication
$65$59
$180
$500
$25
$249
$243
$780$690
$450$419
$70
$440$409
$75
$1,100$1,077.74
$102
$225
$495
$260
$300
$557.57 +$15 Control and authentication
$32
$120
$42$25
$300
$440
$346
$495
$945
$730$679
$105$55.99
$98
$53
$175
$360$335
$98
$98
$98
$339$275
$600$558
$295$265.14
$377.34 +$15 Control and authentication
$98
$98
$98
$240
$240
$261
$62
$225$220
$98
$63
$466
$150
$98
$423
$98
$427
$1,020$883
$990
$55$48
$118
$250
$435
$165
$245
$445
$304
$164$95
$164$95
$72$54
$88
$240
$220
$50
$499
$164$95
$300
$440$409
$285
$494
$300
$300
$180
$300
$180
$399$371
$494
$58
$75
$520$484
$440$409
$62
$930$804
$446
$308
$545$507
$810$700
$810$700
$58
$58
$5,012.48$4,055.04 +$15 Control and authentication
$136
$198$148
$82.73
$313
$208$95
$3,210.24$3,041.28 +$15 Control and authentication
$245
$580$539
$195
$418
$250
$415$375
$465$402
$118
$85
$895$774
$79.99$57.27
$610$567
$450
$779$673
$670$623
$880$761
$225
$658$612
$652$606
$650$605
$75
$499
$120
$710
$167
$475
$660$614
$875
$650$563
$456
$560$485
$389
$103
$220
$366$250
$865 +$15 Control and authentication
$300
$280
$700$598
$595
$48
$350
$350
$325
$650
$170$160
$480 +$15 Control and authentication
$220
$199
$650
$510
$2,480 +$15 Control and authentication
$60
$285
$490$250
$285
$285
$435$425
$600 +$15 Control and authentication
$250
$349 +$15 Control and authentication
$375
$455
$390
$200
$48
$450$370
$484 +$15 Control and authentication
$155$139
$500 +$15 Control and authentication
$438 +$15 Control and authentication
$170$160
$325
$245
$300
$190
$100
$250
$395
$170
$499
$450
$200
$395
$225
$280
$200
$250
$170$160
$100$95
$237
$145$140
$384
$255
$215
$485$399
$405
$299
$300
$250
$250
$220
$198
$350
$150
$100
$190$162
$328
$450
$350
$485
$485
$213
$485
$280
$293
$350
$449
$473 +$15 Control and authentication
$200
$250
$459
$350
$349$325
$375
$275
$248
$1,010
$1,010
$375
$383
$383
$335
$795
$350
$280
$610$550 +$15 Control and authentication
$350
$470 +$15 Control and authentication
$480$250
$595 +$15 Control and authentication
$275$199
$345
$345
$345
$335
$595 +$15 Control and authentication
$605$591 +$15 Control and authentication
$320
$320
$310
$310
Sold at $252 on November 22, 2022
$295
$255$177
$284
$175
$184
$473
$225
$175
$184
$320
$280
$184
$300
$184
$595 +$15 Control and authentication
$595 +$15 Control and authentication
$250
$307
$370
$184
$315
$95$79
$320
$595
$100
$72
$399$398 +$15 Control and authentication
$350
$285 +$15 Control and authentication
$250$221
$220$192
$72
$439
$250$221
$270
Sold at $84
$200
$359
$310
$180 +$15 Control and authentication
$220
$343$260
$342$229
$413$350
$95
$300$268
$275$200
$270
$260$245
$310
$270
$310$299
$275
$178.88$175 +$15 Control and authentication
$300$220
$350
$220
$299
$226.53$192 +$15 Control and authentication
$279
$475
$225
$259
$420$410
$194$178
$24
$345
$250
$345
$105
$320
$300
$1,011 +$15 Control and authentication
$355$333
$379
$661
$1,686 +$15 Control and authentication
$270
$374$345
$110
$295
$385$380
$310
$320
$46
$275
$499 +$15 Control and authentication
$748
$310
$310
$250
$200
$100
$1,064 +$15 Control and authentication
$320
$85$50
$523
$280
$35
$65
$369
$320
$477$450 +$15 Control and authentication
$119$90
$216
$280
$345
$345$320
$190
$399 +$15 Control and authentication
$319
$300
$310
$283
$500$250
$200
$500$349
$295
$310
$300
$325
$320
$320
$325
$325
$320
$299
$335
$399
$319
$345
$185
$374
$219
$285
$215$105
$310
$1,299 +$15 Control and authentication
$359
$260
$135
$310
$320
$320
$325
$325
$403
$345
$239
$345
$309
$35
$310$300
$345
$429
$652
$350
$40
$175
$152$146
$399
$399
$300$276
$499
$329
$200$99
$362
$399
$403
$190.86$179.10 +$15 Control and authentication
$1,329 +$15 Control and authentication
$320
$261
$200
$325
$325
$480$450
$409
$190$170
$288
$1,100 +$15 Control and authentication
$165
$266
$266
$454
$389
$466
$180 +$15 Control and authentication
$85$50
$429
$85$50
$429
$150
$400
$630$586 +$15 Control and authentication
$310
$30$29
$429
$429
$480$378
$374
$188$184
$260$220
$320
$250$68
$449
$206
$180
$288
$70
$40
$325
$310
$275
$225
$28
$199
$78
$345
$316
$447
$582
$900$722
$310
$320
$270
$499$464
$915
$675
$275
$409
$369
$450
$275
$499
$120$96
$290 +$15 Control and authentication
$316
$210
$520
$285
$431
$220
$188
$119
$499$299
$431
$275
$661
$295
$400
$325$290
$450
$160
$285$270
$70
$70
$70
$374$316
$195
$400
$388
$125
$359
$319
$152$146
$145
$239
$195$190
$195$190
$350
$400
$360
$40
$235
$330
$59
$755$537
$250
$374
$275
$500
$379
$403
$265
$399
$203
$300
$377
$405
$438
$200$125
$945
$118
$65
$166$160
$650$532
$355
$70
$70
$518
$538
$879
$342
$309
$290 +$15 Control and authentication
$299
$357
$249
$359
$520
$176
$309
$269
$469
$247
$288$259
$360
$339
$70
$70
$70
$183$177
$143
$41
$259
$190
$293
$1,389 +$15 Control and authentication
$345
$180
$1,287 +$15 Control and authentication
$250
$319
$259
$470
$330
$575
$335
$369
$395$377
$480
$108$98
$359
$1,181
$135
$65
$385
$75
$210$198
$584
$349
$349
$339
$110
$50
$289
$299
$123
$329
$250
$375$370
$339
$219$217
$400
$400
$369
$359
$329
$473
$185
$295$278
$309
$625$616 +$15 Control and authentication
$600$570
$134
$325
$405
$325
$109
$253
$375
$81
$340$299
$55
$285
$2,499 +$15 Control and authentication
$286
$112
$313
$399
$330
$157
$69$49
$310
$325
$325
$891
$233
$119
$45
$450$425
$299
$70
$620
$185.86
$275
$280
$979
$390$386
$1,299 +$15 Control and authentication
$285
$450
$400
$999
$198.83 +$15 Control and authentication
$286
$290$250
$370
$250$225
$295
$133
$133
$309
$485$465
$280
$72$54
$185
$375
$212
$375
$212
$515
$450
$349
$389
$465
$309
$99
$449
$299
$475$375
$300
$309
$585
$329
$440$395
$2,775$1,599 +$15 Control and authentication
$359
$395$370
$235
$185
$400$349
$342
$385$380
$330$299
$269.21 +$15 Control and authentication
$1,299 +$15 Control and authentication
$369
$389
$251
$286
$450
$399
$799$599
$90.94$46.77
$72
$253
$305
$619
$419
$352
$1,068
$350
$99
$458
$950
$293
$104
$370
$399
$749$525
$81
$400
$179
$276
$486
$466
$65
$389$364
$329$309
$223
$89
$234
$550
$415
$484$475
$379
$420
$32.61
$215.67$115.63 +$15 Control and authentication
$96
$134
$360
$189$155
$50
$325
$1,299 +$15 Control and authentication
$595
$290
$349
$356
$570$550
$223
$536
$399$398
$300$288
$600
$309
$405
$284
$100
$255
$135
$295
$599
$329
$58
$750
$420
$310
$96
$495
$495
$77
$1,495$1,295 +$15 Control and authentication
$285
$275
$401
$440
$192$189
$356
$684$650
$895
$536
$360
$536
$150
$375
$300
$80
$500
$400
$795$759
$480$459
$1,095 +$15 Control and authentication
$975
$30$27
$231
$285
$285
$120$83.04
$275
$285
$385
$995$599
$239
$50$29
$179
$400$381
$425
$285
$285
$285
$450
$199
$309
$595
$250
$695
$435$302
$139
$349
$195$115
$379
$855
$795
$45$41
$379
$251
$80
$200
$56
$45
$495
$276
$325
$810
$795
$235
$695
$34
$399
$599$549
$162
$276
$422
$61
$61
$61
$595
$595$499
$99
$119
$385
$563
$563
$199$185
$595
$350
$350
$150$130
$375
$438
$370
$275
$399
$111$84
$144
$350
$350
$98$74
$276
$295
$21
$900$822.40
$239
$585
$90
$445
$400
$22
$170
$320
$320
$335
$105
$350
$325
$267$201
$275
$63
$197.12$168.96 +$15 Control and authentication
$212.89$168.96 +$15 Control and authentication
$595
$100$60
$340$316
$135
$81
$29$22
$459
$358
$333.89 +$15 Control and authentication
$590$575
$625$581
$375$298
$240
$539
$450$360
$81
$250
$184
$498
$400
$82
$680$632
$299
$299
$650
$585
$430$400
$310$288
$420$391
$560$521
$340
$199$129
$400
$45
$175
$400
$298$250
$755$702
$435$405
$425
$399
$45
$60
$63
$345
$45
$45
$50
$57
$400
$608$565
$390$363
$117
$310$288
$148
$260$242
$695$646
$767$713
$146
$57
$57
$351
$59
$60
$61
$61
$61
$61
$61
$49
$84
$145
$105
$136
$128
$128
$157.70 +$15 Control and authentication
$106.53$94.84 +$15 Control and authentication
$439.30 +$15 Control and authentication
$112.64 +$15 Control and authentication
$326.66 +$15 Control and authentication
$416.77$371.71 +$15 Control and authentication
$78.85$70.96 +$15 Control and authentication
$190.60 +$15 Control and authentication
$190.60$157.35 +$15 Control and authentication
$416.77 +$15 Control and authentication
$179.12 +$15 Control and authentication
$190.60 +$15 Control and authentication
$180.27 +$15 Control and authentication
$180.27 +$15 Control and authentication
$563.20 +$15 Control and authentication
$135.17$107.01 +$15 Control and authentication
$175.01 +$15 Control and authentication
$416.77$337.92 +$15 Control and authentication
$225.28 +$15 Control and authentication
Sold at $270.34 on November 22, 2022
$168.96 +$15 Control and authentication
$225.28 +$15 Control and authentication
$225.28$214.02 +$15 Control and authentication
$225.28$214.02 +$15 Control and authentication
$337.92 +$15 Control and authentication
$270.34 +$15 Control and authentication
$112.70 +$15 Control and authentication
$428.03 +$15 Control and authentication
$281.60 +$15 Control and authentication
$505.75 +$15 Control and authentication
$123.90 +$15 Control and authentication
$40.55 +$15 Control and authentication
$45.06 +$15 Control and authentication
$95.74 +$15 Control and authentication
$550.81 +$15 Control and authentication
$411.14 +$15 Control and authentication
$304.13 +$15 Control and authentication
$160.29 +$15 Control and authentication
$411.14 +$15 Control and authentication
$84.48 +$15 Control and authentication
$157.70 +$15 Control and authentication
$51.18$45.13 +$15 Control and authentication
$596.99 +$15 Control and authentication
$377.34 +$15 Control and authentication
$140.80 +$15 Control and authentication
$121.65 +$15 Control and authentication
$168.96 +$15 Control and authentication
$77.72 +$15 Control and authentication
$315.39 +$15 Control and authentication
$197.12 +$15 Control and authentication
$386.36$382.98 +$15 Control and authentication
$225.28 +$15 Control and authentication
$94.15 +$15 Control and authentication
$506.88$337.92 +$15 Control and authentication
$120.52 +$15 Control and authentication
$224.15 +$15 Control and authentication
$90.11$84.48 +$15 Control and authentication
$129.54 +$15 Control and authentication
Sold at $75.18 on November 22, 2022
$135.17$112.64 +$15 Control and authentication
$171.21 +$15 Control and authentication
$247.81$191.49 +$15 Control and authentication
$116.93 +$15 Control and authentication
$90.11 +$15 Control and authentication
$212.89$201.63 +$15 Control and authentication
$259.07 +$15 Control and authentication
$123.08 +$15 Control and authentication
$219.65$168.96 +$15 Control and authentication
$135.17 +$15 Control and authentication
$135.17 +$15 Control and authentication
$73.22$66.46 +$15 Control and authentication
$112.64 +$15 Control and authentication
$336.79 +$15 Control and authentication
$152.06 +$15 Control and authentication
$174.59 +$15 Control and authentication
$112.64 +$15 Control and authentication
$197.12 +$15 Control and authentication
$130 +$15 Control and authentication
$326.66 +$15 Control and authentication
$118.27$90.11 +$15 Control and authentication
$225.28 +$15 Control and authentication
$439.30$426.91 +$15 Control and authentication
$377.34$332.29 +$15 Control and authentication
$112.41 +$15 Control and authentication
$101.34 +$15 Control and authentication
$180.22 +$15 Control and authentication
$79.97$73.22 +$15 Control and authentication
$144.18$126.16 +$15 Control and authentication
$394.24 +$15 Control and authentication
$236.54 +$15 Control and authentication
$450.56 +$15 Control and authentication
$259.07$219.65 +$15 Control and authentication
$80.01$70.44 +$15 Control and authentication
$129.92 +$15 Control and authentication
$140.80$112.64 +$15 Control and authentication
$105.88 +$15 Control and authentication
$168.96 +$15 Control and authentication
$101.38 +$15 Control and authentication
$212.89 +$15 Control and authentication
$112.64 +$15 Control and authentication
$191.49 +$15 Control and authentication
$399.87 +$15 Control and authentication
$52.30 +$15 Control and authentication
$214.02 +$15 Control and authentication
$140.80$123.90 +$15 Control and authentication
$250.06 +$15 Control and authentication
$84.48 +$15 Control and authentication
$104 +$15 Control and authentication
$232.56$228.66 +$15 Control and authentication
$405.50$371.71 +$15 Control and authentication
$279 +$15 Control and authentication
$394.24 +$15 Control and authentication
$428.03$394.24 +$15 Control and authentication
$439.30$315.39 +$15 Control and authentication
$393.11 +$15 Control and authentication
$90.11$72.09 +$15 Control and authentication
$664.58$224.15 +$15 Control and authentication
$405.50$371.71 +$15 Control and authentication
$227.73 +$15 Control and authentication
$361.57$309.76 +$15 Control and authentication
$321.02 +$15 Control and authentication
$197.12 +$15 Control and authentication
$371.71 +$15 Control and authentication
Sold at $411.34 on November 21, 2022
$315.39 +$15 Control and authentication
$508.01$484.35 +$15 Control and authentication
$506.88 +$15 Control and authentication
$304.13 +$15 Control and authentication
$168.96 +$15 Control and authentication
$146.43$135.17 +$15 Control and authentication
$78.85 +$15 Control and authentication
$315.39 +$15 Control and authentication
$78.85$70.96 +$15 Control and authentication
$174.59 +$15 Control and authentication
$225.28 +$15 Control and authentication
$202.75 +$15 Control and authentication
$139.67 +$15 Control and authentication
$84.52$78.89 +$15 Control and authentication
$428.03$405.50 +$15 Control and authentication
$168.96 +$15 Control and authentication
$360.45 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$326.66$304.13 +$15 Control and authentication
$224.15 +$15 Control and authentication
$1,041.92$1,013.76 +$15 Control and authentication
$324.80$259.84 +$15 Control and authentication
$81.10 +$15 Control and authentication
$135.17$107.01 +$15 Control and authentication
$168.96$113.77 +$15 Control and authentication
$95.74 +$15 Control and authentication
$129.54$113.77 +$15 Control and authentication
$191.49 +$15 Control and authentication
$649 +$15 Control and authentication
$209.51$150.94 +$15 Control and authentication
$90.11 +$15 Control and authentication
$377.34 +$15 Control and authentication
$191.49 +$15 Control and authentication
$224.15 +$15 Control and authentication
$81.10 +$15 Control and authentication
$336.79 +$15 Control and authentication
$270.34$241.05 +$15 Control and authentication
$135.17 +$15 Control and authentication
$61.95 +$15 Control and authentication
$490.23 +$15 Control and authentication
$100.25$84.48 +$15 Control and authentication
$61.95 +$15 Control and authentication
$225.28 +$15 Control and authentication
$168.96 +$15 Control and authentication
$304.13$273.72 +$15 Control and authentication
$146.43$107.01 +$15 Control and authentication
$156.74$118.42 +$15 Control and authentication
$337.92$155.44 +$15 Control and authentication
$108.13 +$15 Control and authentication
$259.07 +$15 Control and authentication
$95.74 +$15 Control and authentication
$360.45 +$15 Control and authentication
$394.24$346.93 +$15 Control and authentication
$337.92 +$15 Control and authentication
$281.60$270.34 +$15 Control and authentication
$112.64 +$15 Control and authentication
$336.79$280.47 +$15 Control and authentication
$281.60 +$15 Control and authentication
$281.60 +$15 Control and authentication
$156.74$78.45 +$15 Control and authentication
$156.57$122.78 +$15 Control and authentication
$123.42 +$15 Control and authentication
$281.60 +$15 Control and authentication
$212.89 +$15 Control and authentication
$77.39$47.10 +$15 Control and authentication
$108.58$47.10 +$15 Control and authentication
$85.41$64.36 +$15 Control and authentication
$91.24 +$15 Control and authentication
$225.28 +$15 Control and authentication
$168.96 +$15 Control and authentication
$152.06 +$15 Control and authentication
$157.70 +$15 Control and authentication
$191.49 +$15 Control and authentication
$156.74$78.45 +$15 Control and authentication
$104.34$47.10 +$15 Control and authentication
$123.42 +$15 Control and authentication
$123.42 +$15 Control and authentication
$77.72 +$15 Control and authentication
$191.57$144.62 +$15 Control and authentication
$174.15$63.45 +$15 Control and authentication
$675.84 +$15 Control and authentication
$145.31$122.78 +$15 Control and authentication
$191.49$123.90 +$15 Control and authentication
$315.39 +$15 Control and authentication
$225.28 +$15 Control and authentication
$236.54$214.02 +$15 Control and authentication
$247.81 +$15 Control and authentication
$377.34 +$15 Control and authentication
$382.98 +$15 Control and authentication
$366.08 +$15 Control and authentication
$227.73$213.34 +$15 Control and authentication
$156.74$74.66 +$15 Control and authentication
$101.01$47.10 +$15 Control and authentication
$156.74$78.45 +$15 Control and authentication
$217.40 +$15 Control and authentication
$540.67 +$15 Control and authentication
$387.48$332.29 +$15 Control and authentication
$156.74$78.45 +$15 Control and authentication
$377.34 +$15 Control and authentication
$95.74$79.97 +$15 Control and authentication
$281.60 +$15 Control and authentication
$81.70$76.07 +$15 Control and authentication
$111.51$78.85 +$15 Control and authentication
$67.58 +$15 Control and authentication
$118.27 +$15 Control and authentication
$135.17 +$15 Control and authentication
$315.39$247.81 +$15 Control and authentication
$337.92 +$15 Control and authentication
$382.98 +$15 Control and authentication
$95.74$84.48 +$15 Control and authentication
$180.22$156.57 +$15 Control and authentication
$240$223 +$15 Control and authentication
$104.49$47.10 +$15 Control and authentication
$112.64 +$15 Control and authentication
$309.76 +$15 Control and authentication
$340.17 +$15 Control and authentication
$315.39 +$15 Control and authentication
$145.31 +$15 Control and authentication
$220.86 +$15 Control and authentication
$258.54 +$15 Control and authentication
$142.91 +$15 Control and authentication
$164.45 +$15 Control and authentication
$281.60 +$15 Control and authentication
$168.96$84.48 +$15 Control and authentication
$225.28$193.74 +$15 Control and authentication
$200.94$194.05 +$15 Control and authentication
$298.50$185.86 +$15 Control and authentication
$98 +$15 Control and authentication
$287.23$188.11 +$15 Control and authentication
$202.75$182.48 +$15 Control and authentication
$202.75$182.48 +$15 Control and authentication
$202.75 +$15 Control and authentication
$168.96 +$15 Control and authentication
$405.50$371.71 +$15 Control and authentication
$202.75 +$15 Control and authentication
$202.75 +$15 Control and authentication
$123.42 +$15 Control and authentication
$112.64 +$15 Control and authentication
$95.74$67.58 +$15 Control and authentication
$107.01$90.11 +$15 Control and authentication
$405.50$371.71 +$15 Control and authentication
$232.04 +$15 Control and authentication
$391.99$371.71 +$15 Control and authentication
$107.01 +$15 Control and authentication
$394.24 +$15 Control and authentication
$354.82 +$15 Control and authentication
$197.12$182.48 +$15 Control and authentication
$56.32 +$15 Control and authentication
$292.86$259.07 +$15 Control and authentication
$104.49$74.96 +$15 Control and authentication
$309.76$281.60 +$15 Control and authentication
$428.03 +$15 Control and authentication
$168.96 +$15 Control and authentication
$309.76$275.97 +$15 Control and authentication
$247.81$236.54 +$15 Control and authentication
$197.12 +$15 Control and authentication
$106.50$88.47 +$15 Control and authentication
$140.80 +$15 Control and authentication
$199.37 +$15 Control and authentication
$87.86$77.72 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$253.44 +$15 Control and authentication
$225.28 +$15 Control and authentication
$112.64 +$15 Control and authentication
$197.12$177.97 +$15 Control and authentication
$405.50$371.71 +$15 Control and authentication
$105.88 +$15 Control and authentication
$281.60$224.15 +$15 Control and authentication
$287.23 +$15 Control and authentication
$84.45 +$15 Control and authentication
$315.39$281.60 +$15 Control and authentication
$270.34$202.75 +$15 Control and authentication
$292.86 +$15 Control and authentication
$225 +$15 Control and authentication
$371.71 +$15 Control and authentication
$89.56 +$15 Control and authentication
$84.45 +$15 Control and authentication
$326.66 +$15 Control and authentication
$326.66 +$15 Control and authentication
$118.27 +$15 Control and authentication
$157.70$146.43 +$15 Control and authentication
$360.45 +$15 Control and authentication
Sold at $195.44 on November 22, 2022
$90.11$64.20 +$15 Control and authentication
$244.43 +$15 Control and authentication
$73.22$69.84 +$15 Control and authentication
$163.33$118.27 +$15 Control and authentication
$315.39 +$15 Control and authentication
$50.69 +$15 Control and authentication
$214.37 +$15 Control and authentication
$428.03 +$15 Control and authentication
$134.04 +$15 Control and authentication
$84.45 +$15 Control and authentication
$190.36 +$15 Control and authentication
$50.69 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$97.44 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$97.44 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$168.96$143.05
$405.50$371.71 +$15 Control and authentication
$123.42 +$15 Control and authentication
$123.90$104.76 +$15 Control and authentication
$416.77 +$15 Control and authentication
$156.74$97.22 +$15 Control and authentication
$225.28 +$15 Control and authentication
$156.74$74.66 +$15 Control and authentication
$415.64$408.88 +$15 Control and authentication
$298.50$247.81 +$15 Control and authentication
$208.38 +$15 Control and authentication
$197.12 +$15 Control and authentication
$77.72 +$15 Control and authentication
$84.45 +$15 Control and authentication
$219.65 +$15 Control and authentication
$174.15$84.05 +$15 Control and authentication
$535.04$473.09 +$15 Control and authentication
$174.59 +$15 Control and authentication
$219.65 +$15 Control and authentication
$304.13 +$15 Control and authentication
$140.80 +$15 Control and authentication
$140.80 +$15 Control and authentication
$146.43 +$15 Control and authentication
$95.74$77.72 +$15 Control and authentication
$174.15$84.05 +$15 Control and authentication
$439.30$251.19 +$15 Control and authentication
$202.75$182.48 +$15 Control and authentication
$253.34$188.38 +$15 Control and authentication
$348.06$326.66 +$15 Control and authentication
$200$155 +$15 Control and authentication
$70.96$64.20 +$15 Control and authentication
$191.49 +$15 Control and authentication
$371.71$300.75 +$15 Control and authentication
$422.40$416.77 +$15 Control and authentication
$326.66$319.90 +$15 Control and authentication
$156.74$74.66 +$15 Control and authentication
$97.44 +$15 Control and authentication
$156.74$97.22 +$15 Control and authentication
$185.86$150.94 +$15 Control and authentication
$110.43 +$15 Control and authentication
$275.97$269.21 +$15 Control and authentication
$168.96$166.71 +$15 Control and authentication
$159.95 +$15 Control and authentication
$194.88 +$15 Control and authentication
$359$329 +$15 Control and authentication
$123.42 +$15 Control and authentication
$125.39$78.45 +$15 Control and authentication
$103.94 +$15 Control and authentication
$280.47$129.54 +$15 Control and authentication
$146.43 +$15 Control and authentication
Sold at $84.48 on November 22, 2022
$326.66 +$15 Control and authentication
$416.77$360.45 +$15 Control and authentication
$225.28$202.75 +$15 Control and authentication
$281.60 +$15 Control and authentication
$98 +$15 Control and authentication
$84.45 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$582.87$429.87 +$15 Control and authentication
$84.48 +$15 Control and authentication
$233.85 +$15 Control and authentication
$112.64 +$15 Control and authentication
$461.82 +$15 Control and authentication
$111.51 +$15 Control and authentication
$140.80$107.01 +$15 Control and authentication
Sold at $399.25 on November 22, 2022
$174.59$141.93 +$15 Control and authentication
$450.56 +$15 Control and authentication
$259.07$244.43 +$15 Control and authentication
$202.75$111.51 +$15 Control and authentication
$388.61 +$15 Control and authentication
$253.44$175.72 +$15 Control and authentication
$123.42 +$15 Control and authentication
$152.06 +$15 Control and authentication
$191.49 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$505.75$483.23 +$15 Control and authentication
$506.88$377.34 +$15 Control and authentication
$84.45 +$15 Control and authentication
$354.82 +$15 Control and authentication
$156.74$74.66 +$15 Control and authentication
$156.74$74.66 +$15 Control and authentication
$72.86 +$15 Control and authentication
$73.22$66.46 +$15 Control and authentication
$202.75 +$15 Control and authentication
$253.57 +$15 Control and authentication
$290.61$279.35 +$15 Control and authentication
$280.47 +$15 Control and authentication
Sold at $105 on November 23, 2022
$129.54$101.38 +$15 Control and authentication
$219.65 +$15 Control and authentication
Sold at $45.45 on November 21, 2022
$509.13$484.35 +$15 Control and authentication
$180.22$157.70 +$15 Control and authentication
$152.06$137.42 +$15 Control and authentication
$449.43 +$15 Control and authentication
$407.76 +$15 Control and authentication
$84.45 +$15 Control and authentication
$84.45 +$15 Control and authentication
$21.13 +$15 Control and authentication
$84.45 +$15 Control and authentication
$88.99 +$15 Control and authentication
$336.79$326.66 +$15 Control and authentication
$214.02 +$15 Control and authentication
$110.43 +$15 Control and authentication
$405.50$360.45 +$15 Control and authentication
$649.60 +$15 Control and authentication
$360.45 +$15 Control and authentication
$146.43$112.64 +$15 Control and authentication
$50.69$36.04 +$15 Control and authentication
$59.17$52.12 +$15 Control and authentication
$394.24 +$15 Control and authentication
$93.49$70.96 +$15 Control and authentication
$180.22$135.17 +$15 Control and authentication
$100.25$69.84 +$15 Control and authentication
$256.42 +$15 Control and authentication
$77.72 +$15 Control and authentication
$73.22 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$1,520.64 +$15 Control and authentication
$456.19 +$15 Control and authentication
$202.75 +$15 Control and authentication
$145.31 +$15 Control and authentication
$112.64 +$15 Control and authentication
$123.90$83.35 +$15 Control and authentication
$449.43 +$15 Control and authentication
$90 +$15 Control and authentication
$95.74$67.58 +$15 Control and authentication
$349.18 +$15 Control and authentication
$112.70$80.30 +$15 Control and authentication
$309.76$299.62 +$15 Control and authentication
$377.34$256.82 +$15 Control and authentication
$506.88 +$15 Control and authentication
$135.17 +$15 Control and authentication
$67.58$65.33 +$15 Control and authentication
$270.34$259.07 +$15 Control and authentication
$205.03 +$15 Control and authentication
$200.50 +$15 Control and authentication
$259.07 +$15 Control and authentication
$146.43 +$15 Control and authentication
$197.12 +$15 Control and authentication
$394.24$360.45 +$15 Control and authentication
$732.16$315.39 +$15 Control and authentication
$336.79 +$15 Control and authentication
$208.38 +$15 Control and authentication
$220.86 +$15 Control and authentication
$111.51$83.35 +$15 Control and authentication
$67.62$57.76 +$15 Control and authentication
$225.28 +$15 Control and authentication
$407.76 +$15 Control and authentication
$253.44 +$15 Control and authentication
$563.20$506.88 +$15 Control and authentication
$461.82$433.66 +$15 Control and authentication
$111.51$107.01 +$15 Control and authentication
$107.01$101.38 +$15 Control and authentication
$197.12 +$15 Control and authentication
$270.34 +$15 Control and authentication
$212.89 +$15 Control and authentication
$315.39 +$15 Control and authentication
$168.96 +$15 Control and authentication
$136.29$112.64 +$15 Control and authentication
$326.66$238.80 +$15 Control and authentication
$168.96$163.33 +$15 Control and authentication
$191.49 +$15 Control and authentication
$450.56$328.91 +$15 Control and authentication
$247.81 +$15 Control and authentication
$439.30 +$15 Control and authentication
$201.63 +$15 Control and authentication
$168.96$163.33 +$15 Control and authentication
$506.88 +$15 Control and authentication
$202.75$168.96 +$15 Control and authentication
$157.70 +$15 Control and authentication
$157.70 +$15 Control and authentication
$299.64$287.65 +$15 Control and authentication
$506.88$474.21 +$15 Control and authentication
$292.86 +$15 Control and authentication
$191.49 +$15 Control and authentication
$428.03$349.18 +$15 Control and authentication
$360.45$291.74 +$15 Control and authentication
$545.66$441.73 +$15 Control and authentication
$619.52$596.99 +$15 Control and authentication
$491.11 +$15 Control and authentication
$157.70 +$15 Control and authentication
$225.28 +$15 Control and authentication
$360.45$291.74 +$15 Control and authentication
$73.22 +$15 Control and authentication
$71.46 +$15 Control and authentication
$77.48$74.66 +$15 Control and authentication
$95.74$50.69 +$15 Control and authentication
$212.89 +$15 Control and authentication
$67.62$63.39 +$15 Control and authentication
$506.88 +$15 Control and authentication
$174.15$84.05 +$15 Control and authentication
$214.02$146.43 +$15 Control and authentication
$411.14$406.63 +$15 Control and authentication
$281.60 +$15 Control and authentication
$224.15$208.38 +$15 Control and authentication
$233.85$214.37 +$15 Control and authentication
$168.96$91.24 +$15 Control and authentication
$58.57 +$15 Control and authentication
$225.28 +$15 Control and authentication
$281.60 +$15 Control and authentication
$103.63 +$15 Control and authentication
$391.99$387.48 +$15 Control and authentication
$253.44 +$15 Control and authentication
$450.56 +$15 Control and authentication
Sold at $159.08 on November 22, 2022
$167.83 +$15 Control and authentication
$88.99 +$15 Control and authentication
$56.32$50.69 +$15 Control and authentication
$129.54$52.94 +$15 Control and authentication
$360.45$291.74 +$15 Control and authentication
$405.50$371.71 +$15 Control and authentication
$551.94$439.30 +$15 Control and authentication
$168.96 +$15 Control and authentication
$107.01$56.32 +$15 Control and authentication
$325.53$275.97 +$15 Control and authentication
$1,408$1,141.04 +$15 Control and authentication
$435.92$431.41 +$15 Control and authentication
$76.71 +$15 Control and authentication
$901.12$732.16 +$15 Control and authentication
$287.65$191.77 +$15 Control and authentication
$233.85$220.86 +$15 Control and authentication
$370.59$353.69 +$15 Control and authentication
$226.06$224.76 +$15 Control and authentication
$274.84$223.03 +$15 Control and authentication
Sold at $68.18 on November 21, 2022
$214.02$146.43 +$15 Control and authentication
$214.02$157.70 +$15 Control and authentication
$95.74 +$15 Control and authentication
$377.34 +$15 Control and authentication
$207.87$85.75 +$15 Control and authentication
$66.46$46.18 +$15 Control and authentication
$390.86$382.98 +$15 Control and authentication
$394.24$360.45 +$15 Control and authentication
$444.93 +$15 Control and authentication
$253.44 +$15 Control and authentication
$439.30 +$15 Control and authentication
$100.25 +$15 Control and authentication
$156.57$100.25 +$15 Control and authentication
$162.20$129.54 +$15 Control and authentication
$108.13$96.87 +$15 Control and authentication
$185.86 +$15 Control and authentication
$957.92 +$15 Control and authentication
$88.99 +$15 Control and authentication
$225.28 +$15 Control and authentication
$114.94$84.05 +$15 Control and authentication
$136.29 +$15 Control and authentication
$405.50 +$15 Control and authentication
$360.45 +$15 Control and authentication
$103.63 +$15 Control and authentication
$439.30 +$15 Control and authentication
$405.50 +$15 Control and authentication
$394.24 +$15 Control and authentication
$506.88$439.30 +$15 Control and authentication
$506.88 +$15 Control and authentication
$394.24 +$15 Control and authentication
$69.84$58.57 +$15 Control and authentication
$225.28$175.72 +$15 Control and authentication
$719.33$681.47 +$15 Control and authentication
$394.24 +$15 Control and authentication
$315.39$274.84 +$15 Control and authentication
$229.64 +$15 Control and authentication
$215.14$135.17 +$15 Control and authentication
Sold at $56.32 on November 22, 2022
$152.06$123.90 +$15 Control and authentication
Sold at $321.02 on November 22, 2022
$217.40$193.74 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$450.56 +$15 Control and authentication
$78.85$56.32 +$15 Control and authentication
$280.47 +$15 Control and authentication
$107.01$81.10 +$15 Control and authentication
$394.24$393.11 +$15 Control and authentication
$58.46$51.97 +$15 Control and authentication
$168.96 +$15 Control and authentication
$73.22$66.46 +$15 Control and authentication
$101.38 +$15 Control and authentication
$224.15 +$15 Control and authentication
$377.34 +$15 Control and authentication
$377.34 +$15 Control and authentication
$191.49$132.92 +$15 Control and authentication
$405.50 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$135.17$123.90 +$15 Control and authentication
$337.92 +$15 Control and authentication
$247.81 +$15 Control and authentication
$225.28 +$15 Control and authentication
$422.40 +$15 Control and authentication
$224.15 +$15 Control and authentication
$111.51$100.25 +$15 Control and authentication
$1,550 +$15 Control and authentication
$506.88 +$15 Control and authentication
$111.51 +$15 Control and authentication
$439.30 +$15 Control and authentication
$405.50 +$15 Control and authentication
$56.32 +$15 Control and authentication
$450.56 +$15 Control and authentication
$291.44$273.22 +$15 Control and authentication
$208.38 +$15 Control and authentication
$259.07$182.48 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$405.50 +$15 Control and authentication
$439.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$405.50 +$15 Control and authentication
$405.50 +$15 Control and authentication
$104.76 +$15 Control and authentication
$55.19 +$15 Control and authentication
$405.50 +$15 Control and authentication
$168.96$152.06 +$15 Control and authentication
$450.56 +$15 Control and authentication
$337.92 +$15 Control and authentication
$120.52$90.11 +$15 Control and authentication
$439.30 +$15 Control and authentication
$135.17$108.13 +$15 Control and authentication
$439.30 +$15 Control and authentication
$337.92 +$15 Control and authentication
$145.31 +$15 Control and authentication
$185.86$167.83 +$15 Control and authentication
$337.79$253.34 +$15 Control and authentication
$407.76 +$15 Control and authentication
$394.24 +$15 Control and authentication
$382.98$366.08 +$15 Control and authentication
$214.02$168.96 +$15 Control and authentication
$123.90 +$15 Control and authentication
$405.50 +$15 Control and authentication
$439.30 +$15 Control and authentication
$484.35$461.82 +$15 Control and authentication
$168.96 +$15 Control and authentication
$142.91 +$15 Control and authentication
$304.13$225.28 +$15 Control and authentication
$214.02 +$15 Control and authentication
$324.80$298.81 +$15 Control and authentication
$299$215 +$15 Control and authentication
$224.15 +$15 Control and authentication
$167.83$157.70 +$15 Control and authentication
$371.71$354.82 +$15 Control and authentication
$202.75 +$15 Control and authentication
$163.33$87.86 +$15 Control and authentication
$168.96 +$15 Control and authentication
$1,464.32$675.84 +$15 Control and authentication
$69.98 +$15 Control and authentication
$111.51 +$15 Control and authentication
$692.74 +$15 Control and authentication
$281.60$230.91 +$15 Control and authentication
$45.06 +$15 Control and authentication
$197 +$15 Control and authentication
$394.24$157.70 +$15 Control and authentication
$67.58$61.95 +$15 Control and authentication
$291.44$273.22 +$15 Control and authentication
$201.63 +$15 Control and authentication
$585.73 +$15 Control and authentication
$247.81 +$15 Control and authentication
$168.96$123.90 +$15 Control and authentication
$168.96 +$15 Control and authentication
Sold at $77.27 on November 22, 2022
$88.99 +$15 Control and authentication
$152.06 +$15 Control and authentication
$90.11$55.19 +$15 Control and authentication
$332.29 +$15 Control and authentication
$360.45 +$15 Control and authentication
$360.45 +$15 Control and authentication
$487.20$324.80 +$15 Control and authentication
$449.43 +$15 Control and authentication
$281.60 +$15 Control and authentication
$387.48 +$15 Control and authentication
$215.14 +$15 Control and authentication
$336.79 +$15 Control and authentication
$394.24 +$15 Control and authentication
$738.72 +$15 Control and authentication
$90.11 +$15 Control and authentication
$332.29$321.02 +$15 Control and authentication
$369$338 +$15 Control and authentication
$281.60$163.33 +$15 Control and authentication
$584.64$406.65 +$15 Control and authentication
$618.39$494.49 +$15 Control and authentication
$366.08$337.92 +$15 Control and authentication
$77.72 +$15 Control and authentication
$449.43$439.30 +$15 Control and authentication
$428.03 +$15 Control and authentication
$101.38 +$15 Control and authentication
$327.24$264.09 +$15 Control and authentication
$214.02$202.75 +$15 Control and authentication
$337.92 +$15 Control and authentication
$388.46$370.27 +$15 Control and authentication
$394.24 +$15 Control and authentication
$81.10$66.46 +$15 Control and authentication
$595.87 +$15 Control and authentication
$78.85 +$15 Control and authentication
$326.66$322.15 +$15 Control and authentication
$63.08 +$15 Control and authentication
$535.31$450.79 +$15 Control and authentication
$461.82$456.19 +$15 Control and authentication
$168.96$140.80 +$15 Control and authentication
$449.43 +$15 Control and authentication
$246.68 +$15 Control and authentication
$179.78$174.99 +$15 Control and authentication
$467.46$354.82 +$15 Control and authentication
$180.22 +$15 Control and authentication
$125.03$113.77 +$15 Control and authentication
$129.54 +$15 Control and authentication
$219.65$202.75 +$15 Control and authentication
$146.43$140.80 +$15 Control and authentication
$304.13$281.60 +$15 Control and authentication
$337.92$332.29 +$15 Control and authentication
$232.56 +$15 Control and authentication
$84.48$73.22 +$15 Control and authentication
$281.60 +$15 Control and authentication
$371.71$336.79 +$15 Control and authentication
$202.75$180.22 +$15 Control and authentication
$287.05$195.20 +$15 Control and authentication
$264.70 +$15 Control and authentication
$129.54 +$15 Control and authentication
$168.96 +$15 Control and authentication
$168.96$123.90 +$15 Control and authentication
$242.18$185.86 +$15 Control and authentication
$201.63$171.21 +$15 Control and authentication
$225.28 +$15 Control and authentication
$168.96$152.06 +$15 Control and authentication
$168.96$134.04 +$15 Control and authentication
$394.24 +$15 Control and authentication
$168.96 +$15 Control and authentication
$77.95$57.16 +$15 Control and authentication
$134.04$95.74 +$15 Control and authentication
$152.06$127.28 +$15 Control and authentication
$123.90$118.27 +$15 Control and authentication
$219.65$208.38 +$15 Control and authentication
$394.24 +$15 Control and authentication
$281.60$242.18 +$15 Control and authentication
$236.54 +$15 Control and authentication
$112.64 +$15 Control and authentication
$180.22$162.20 +$15 Control and authentication
$326.66$303 +$15 Control and authentication
$123.90 +$15 Control and authentication
$280.47$202.75 +$15 Control and authentication
$225.28$168.96 +$15 Control and authentication
$102.50 +$15 Control and authentication
$337.92 +$15 Control and authentication
$78.85$70.96 +$15 Control and authentication
$168.96$118.27 +$15 Control and authentication
$382.98$366.08 +$15 Control and authentication
$377.34$360.45 +$15 Control and authentication
$388.61 +$15 Control and authentication
$152.06 +$15 Control and authentication
$100.25$91.24 +$15 Control and authentication
$212.89 +$15 Control and authentication
$99.12 +$15 Control and authentication
$320$220 +$15 Control and authentication
$281.60 +$15 Control and authentication
$163.33 +$15 Control and authentication
$57.45$25.91 +$15 Control and authentication
$168.96 +$15 Control and authentication
$377.34 +$15 Control and authentication
$304.13$274.84 +$15 Control and authentication
$201.02$181.02 +$15 Control and authentication
$101.38 +$15 Control and authentication
$138.55 +$15 Control and authentication
$469.94 +$15 Control and authentication
$281.60$236.54 +$15 Control and authentication
$394.24$259.07 +$15 Control and authentication
$129.54$107.01 +$15 Control and authentication
$77.48$53.53 +$15 Control and authentication
$619.52 +$15 Control and authentication
$515.89$506.88 +$15 Control and authentication
$315.39$271.46 +$15 Control and authentication
$433.66 +$15 Control and authentication
$366.08$292.86 +$15 Control and authentication
$225.28$170.09 +$15 Control and authentication
$253.57$190.18 +$15 Control and authentication
$61.95 +$15 Control and authentication
$180.22 +$15 Control and authentication
$168.96$126.16 +$15 Control and authentication
$152.06$98 +$15 Control and authentication
$164.45 +$15 Control and authentication
$1,070.08 +$15 Control and authentication
$389.76$253.34 +$15 Control and authentication
$168.96$152.06 +$15 Control and authentication
$280.47 +$15 Control and authentication
$202.75 +$15 Control and authentication
$224.15 +$15 Control and authentication
$168.96$121.65 +$15 Control and authentication
$202.75 +$15 Control and authentication
$214.02$191.49 +$15 Control and authentication
$461.82 +$15 Control and authentication
$281.60 +$15 Control and authentication
$506.88$450.56 +$15 Control and authentication
$377.34$360.45 +$15 Control and authentication
$444.93$424.65 +$15 Control and authentication
$281.60$191.49 +$15 Control and authentication
$385.23 +$15 Control and authentication
$73.22$67.58 +$15 Control and authentication
$292.86$280.47 +$15 Control and authentication
$382.98$281.60 +$15 Control and authentication
$247.81$212.89 +$15 Control and authentication
$280.47 +$15 Control and authentication
$450.56 +$15 Control and authentication
$337.92 +$15 Control and authentication
$107.39$97.05 +$15 Control and authentication
$405.50 +$15 Control and authentication
$422.40 +$15 Control and authentication
$292.86$263.58 +$15 Control and authentication
$137.42$123.90 +$15 Control and authentication
$439.30$422.40 +$15 Control and authentication
$172.34 +$15 Control and authentication
$140.80$110.39 +$15 Control and authentication
$281.60$253.44 +$15 Control and authentication
$508.01$506.88 +$15 Control and authentication
$99$79 +$15 Control and authentication
$197.12$168.96 +$15 Control and authentication
$506.88 +$15 Control and authentication
$377.34$343.55 +$15 Control and authentication
$281.60 +$15 Control and authentication
$306.38 +$15 Control and authentication
$88.99 +$15 Control and authentication
$374.17$350.78 +$15 Control and authentication
$394.24 +$15 Control and authentication
$382.98$366.08 +$15 Control and authentication
$224.15 +$15 Control and authentication
$250.06$229.79 +$15 Control and authentication
$155.90 +$15 Control and authentication
$253.34 +$15 Control and authentication
$163.33$123.90 +$15 Control and authentication
$177.97 +$15 Control and authentication
$90.11$74.34 +$15 Control and authentication
$315.39$283.85 +$15 Control and authentication
$227.36$175.39 +$15 Control and authentication
$101.38 +$15 Control and authentication
$349.18 +$15 Control and authentication
$87.86 +$15 Control and authentication
$157.70$135.17 +$15 Control and authentication
$411.14 +$15 Control and authentication
$101.38$86.17 +$15 Control and authentication
$337.92$293.99 +$15 Control and authentication
$281.60 +$15 Control and authentication
$281.60$180.22 +$15 Control and authentication
$444.93$337.92 +$15 Control and authentication
$145.72 +$15 Control and authentication
$437.04$428.03 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$101.38$75.47 +$15 Control and authentication
$337.79 +$15 Control and authentication
$844.80$788.48 +$15 Control and authentication
$123.90$81.10 +$15 Control and authentication
$382.98$366.08 +$15 Control and authentication
$168.96 +$15 Control and authentication
$150$63 +$15 Control and authentication
$416.77$202.75 +$15 Control and authentication
$292.86 +$15 Control and authentication
$315.39$247.81 +$15 Control and authentication
$129.54 +$15 Control and authentication
$314.27$291.74 +$15 Control and authentication
$134.04$120.52 +$15 Control and authentication
$110.39$81.10 +$15 Control and authentication
$326.66 +$15 Control and authentication
$399.87 +$15 Control and authentication
$123.90 +$15 Control and authentication
$219.65$180.22 +$15 Control and authentication
$90$80 +$15 Control and authentication
$107.01$67.58 +$15 Control and authentication
$414.52 +$15 Control and authentication
$613.47 +$15 Control and authentication
$107.87$95.88 +$15 Control and authentication
$253.44 +$15 Control and authentication
$540.67 +$15 Control and authentication
$508.01$484.35 +$15 Control and authentication
$66.46 +$15 Control and authentication
$214.02 +$15 Control and authentication
$75.47$67.58 +$15 Control and authentication
$225.28$123.90 +$15 Control and authentication
$247.81 +$15 Control and authentication
$343.55 +$15 Control and authentication
$180.22$159.95 +$15 Control and authentication
$224.15 +$15 Control and authentication
$209.51 +$15 Control and authentication
$157.70$135.17 +$15 Control and authentication
$100.25$79.97 +$15 Control and authentication
$261.23$134.93 +$15 Control and authentication
$337.92 +$15 Control and authentication
$281.60 +$15 Control and authentication
$67.58 +$15 Control and authentication
$394.24$315.39 +$15 Control and authentication
$292.86 +$15 Control and authentication
$135.17 +$15 Control and authentication
$321.02$279.35 +$15 Control and authentication
$257.95 +$15 Control and authentication
$377.34$360.45 +$15 Control and authentication
$366.08$337.92 +$15 Control and authentication
$127.32 +$15 Control and authentication
$183.60 +$15 Control and authentication
$281.60$263.58 +$15 Control and authentication
$112.64$109.26 +$15 Control and authentication
$114.89$93.49 +$15 Control and authentication
$337.92$278.22 +$15 Control and authentication
$394.24$382.98 +$15 Control and authentication
$43.93 +$15 Control and authentication
$506.88 +$15 Control and authentication
$165 +$15 Control and authentication
$163.33 +$15 Control and authentication
$90.11$84.48 +$15 Control and authentication
$129.54$50.69 +$15 Control and authentication
$281.60$236.54 +$15 Control and authentication
$332.29 +$15 Control and authentication
$78.85$67.58 +$15 Control and authentication
$253.44 +$15 Control and authentication
$585.73 +$15 Control and authentication
$270.34 +$15 Control and authentication
$270.34 +$15 Control and authentication
$270.34 +$15 Control and authentication
$450.56 +$15 Control and authentication
$270.34 +$15 Control and authentication
$162.40$145.51 +$15 Control and authentication
$214.02 +$15 Control and authentication
$377.34 +$15 Control and authentication
$163.33 +$15 Control and authentication
$267.19 +$15 Control and authentication
$154.96 +$15 Control and authentication
$162.40$84.45 +$15 Control and authentication
$619.52$292.86 +$15 Control and authentication
$225.28 +$15 Control and authentication
$506.88$304.13 +$15 Control and authentication
$112.64 +$15 Control and authentication
$50.69 +$15 Control and authentication
$167.83 +$15 Control and authentication
$100.25 +$15 Control and authentication
$382.98$371.71 +$15 Control and authentication
$321.18$259.48 +$15 Control and authentication
$281.60 +$15 Control and authentication
$67.58$60.83 +$15 Control and authentication
$168.96 +$15 Control and authentication
$619.52$411.14 +$15 Control and authentication
$336.79 +$15 Control and authentication
$428.03$349.18 +$15 Control and authentication
$303 +$15 Control and authentication
$337.92$163.33 +$15 Control and authentication
$404.38 +$15 Control and authentication
$292.86$275.97 +$15 Control and authentication
$202.75 +$15 Control and authentication
$129.54$117.15 +$15 Control and authentication
$394.24$259.07 +$15 Control and authentication
$168.96 +$15 Control and authentication
$163.33 +$15 Control and authentication
$405.50$281.60 +$15 Control and authentication
$360.45 +$15 Control and authentication
$281.60 +$15 Control and authentication
$281.60 +$15 Control and authentication
$225.28$202.75 +$15 Control and authentication
$214.02 +$15 Control and authentication
$247.81 +$15 Control and authentication
$58.46 +$15 Control and authentication
$219.65 +$15 Control and authentication
$100.25 +$15 Control and authentication
$357.28$302.71 +$15 Control and authentication
$146.43 +$15 Control and authentication
$619.52$448.31 +$15 Control and authentication
$146.43 +$15 Control and authentication
$199$179 +$15 Control and authentication
$246.68$219.65 +$15 Control and authentication
$87.86 +$15 Control and authentication
$67.58 +$15 Control and authentication
$635.29$560.95 +$15 Control and authentication
$67.58 +$15 Control and authentication
$247.81 +$15 Control and authentication
$281.60 +$15 Control and authentication
$280.47 +$15 Control and authentication
$196.18$155.90 +$15 Control and authentication
$563.20$262.45 +$15 Control and authentication
$239.71 +$15 Control and authentication
$420 +$15 Control and authentication
$350.31 +$15 Control and authentication
$185.86$166.71 +$15 Control and authentication
$357.28 +$15 Control and authentication
$301.88 +$15 Control and authentication
$449.43 +$15 Control and authentication
$394.24$377.34 +$15 Control and authentication
$154.32$153.19 +$15 Control and authentication
$146.43 +$15 Control and authentication
$363.77$309.21 +$15 Control and authentication
$95.74$63.08 +$15 Control and authentication
$284.98$247.81 +$15 Control and authentication
$223.03 +$15 Control and authentication
$350$211 +$15 Control and authentication
$236.54$225.28 +$15 Control and authentication
$101.38$78.85 +$15 Control and authentication
$87.86$78.85 +$15 Control and authentication
$163.33 +$15 Control and authentication
$247.81 +$15 Control and authentication
$405.50 +$15 Control and authentication
$152.06 +$15 Control and authentication
$350.78$297.52 +$15 Control and authentication
$377.34 +$15 Control and authentication
$202.75$112.64 +$15 Control and authentication
$192.41 +$15 Control and authentication
$675.84 +$15 Control and authentication
$71.46 +$15 Control and authentication
$101.38$92.36 +$15 Control and authentication
$428.03 +$15 Control and authentication
$315.39 +$15 Control and authentication
$433.66$428.03 +$15 Control and authentication
$303 +$15 Control and authentication
$146.43$135.17 +$15 Control and authentication
$212.89 +$15 Control and authentication
$439.30 +$15 Control and authentication
$405.50$377.34 +$15 Control and authentication
$388.61$354.82 +$15 Control and authentication
$619.52$506.88 +$15 Control and authentication
$281.60$253.44 +$15 Control and authentication
$407.76 +$15 Control and authentication
$67.56 +$15 Control and authentication
$377.34 +$15 Control and authentication
$84.48$56.32 +$15 Control and authentication
$134.04$108.13 +$15 Control and authentication
$415.64$394.24 +$15 Control and authentication
$145.31$114.89 +$15 Control and authentication
$135.17 +$15 Control and authentication
$281.60 +$15 Control and authentication
Sold at $431.79 on November 21, 2022
$336.79 +$15 Control and authentication
$73.22$61.95 +$15 Control and authentication
Sold at $62.50 on November 21, 2022
$129.92$90.94 +$15 Control and authentication
$449.43 +$15 Control and authentication
$168.96$152.06 +$15 Control and authentication
$957.44$698.37 +$15 Control and authentication
$82.23$73.22 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$343.55$326.66 +$15 Control and authentication
$366.08$337.92 +$15 Control and authentication
$100.25$52.94 +$15 Control and authentication
$382.98$360.45 +$15 Control and authentication
$140.80$129.54 +$15 Control and authentication
$407.76 +$15 Control and authentication
$214.02$155.44 +$15 Control and authentication
$360.45 +$15 Control and authentication
$439.30 +$15 Control and authentication
$45.06$39.42 +$15 Control and authentication
$123.90$73.22 +$15 Control and authentication
$377.34$343.55 +$15 Control and authentication
$399.87$360.45 +$15 Control and authentication
$354.82 +$15 Control and authentication
$219.65 +$15 Control and authentication
$500.19 +$15 Control and authentication
$146.43 +$15 Control and authentication
$281.60 +$15 Control and authentication
$337.92 +$15 Control and authentication
$163.33 +$15 Control and authentication
$181.89$62.36 +$15 Control and authentication
$349.18$332.29 +$15 Control and authentication
$354.82 +$15 Control and authentication
$112.64 +$15 Control and authentication
$360.45$348.06 +$15 Control and authentication
$168.96$157.70 +$15 Control and authentication
$270.34 +$15 Control and authentication
$292.86$263.58 +$15 Control and authentication
$168.96$70.96 +$15 Control and authentication
$385.23 +$15 Control and authentication
$360.45 +$15 Control and authentication
$177.66 +$15 Control and authentication
$67.58 +$15 Control and authentication
$168.96 +$15 Control and authentication
$377.34$321.02 +$15 Control and authentication
$349.18 +$15 Control and authentication
$149.41$142.91 +$15 Control and authentication
$63.39 +$15 Control and authentication
$233.48 +$15 Control and authentication
$377.34$340.17 +$15 Control and authentication
$450.56$411.14 +$15 Control and authentication
$508.01$484.35 +$15 Control and authentication
$371.71$360.45 +$15 Control and authentication
$168.96$157.70 +$15 Control and authentication
$332.29 +$15 Control and authentication
$506.88 +$15 Control and authentication
$619.52 +$15 Control and authentication
$326.66 +$15 Control and authentication
$550.81$483.23 +$15 Control and authentication
$257.95 +$15 Control and authentication
$70.96$60.83 +$15 Control and authentication
$354.82 +$15 Control and authentication
$394.24$324.40 +$15 Control and authentication
$208.38 +$15 Control and authentication
$287.05 +$15 Control and authentication
$280.47 +$15 Control and authentication
$270.34$214.02 +$15 Control and authentication
$360.45 +$15 Control and authentication
$349.18$326.66 +$15 Control and authentication
$360.45$354.82 +$15 Control and authentication
$315.39$281.60 +$15 Control and authentication
$168.96 +$15 Control and authentication
$381.85 +$15 Control and authentication
$75$54 +$15 Control and authentication
$123.30 +$15 Control and authentication
$281.60 +$15 Control and authentication
$675.84 +$15 Control and authentication
$100.25 +$15 Control and authentication
$257.95 +$15 Control and authentication
$349.18 +$15 Control and authentication
$112.64$111.51 +$15 Control and authentication
$371.71$292.86 +$15 Control and authentication
$214.02$145.31 +$15 Control and authentication
$284.98$247.81 +$15 Control and authentication
$574.11$436.32 +$15 Control and authentication
$399.87$343.55 +$15 Control and authentication
$315.39 +$15 Control and authentication
$377.34$371.71 +$15 Control and authentication
$179.10 +$15 Control and authentication
$422.40 +$15 Control and authentication
$449.43 +$15 Control and authentication
$399.87$326.66 +$15 Control and authentication
$200 +$15 Control and authentication
$394.24 +$15 Control and authentication
$280.47 +$15 Control and authentication
$214.02$146.43 +$15 Control and authentication
$123.90$90.11 +$15 Control and authentication
$168.96$112.64 +$15 Control and authentication
$371.71 +$15 Control and authentication
$197.12$152.06 +$15 Control and authentication
$394.24 +$15 Control and authentication
$168.96$123.90 +$15 Control and authentication
$95.74$51.81 +$15 Control and authentication
$563.20$422.40 +$15 Control and authentication
$146.43 +$15 Control and authentication
$499$484.35 +$15 Control and authentication
$103.63 +$15 Control and authentication
$732.16$619.52 +$15 Control and authentication
$309.76$305.25 +$15 Control and authentication
$506.88 +$15 Control and authentication
Sold at $39.42 on November 23, 2022
$247.81 +$15 Control and authentication
$155.81 +$15 Control and authentication
$58.46 +$15 Control and authentication
$94.62 +$15 Control and authentication
$343.55$326.66 +$15 Control and authentication
$655.56$584.60 +$15 Control and authentication
$208.38 +$15 Control and authentication
$191.49$172.34 +$15 Control and authentication
$506.88 +$15 Control and authentication
$370.59$348.06 +$15 Control and authentication
$506.88 +$15 Control and authentication
$349.18 +$15 Control and authentication
$336.79 +$15 Control and authentication
$349.18 +$15 Control and authentication
$214.02$146.43 +$15 Control and authentication
$247.81 +$15 Control and authentication
$388.61$382.98 +$15 Control and authentication
$191.49$155.44 +$15 Control and authentication
$434.79$214.02 +$15 Control and authentication
$197.22 +$15 Control and authentication
$70$50 +$15 Control and authentication
$280.47$129.54 +$15 Control and authentication
$951.81 +$15 Control and authentication
$225.28 +$15 Control and authentication
$506.88 +$15 Control and authentication
$551.94$495.62 +$15 Control and authentication
$155.90$149.41 +$15 Control and authentication
$78.85 +$15 Control and authentication
$371.71$369.46 +$15 Control and authentication
$354.82$326.66 +$15 Control and authentication
$360.45$304.13 +$15 Control and authentication
$411.14$377.34 +$15 Control and authentication
$405.50$394.24 +$15 Control and authentication
$394.24$349.18 +$15 Control and authentication
$416.77$379.60 +$15 Control and authentication
$225.28 +$15 Control and authentication
$112.64 +$15 Control and authentication
$84.48$77.72 +$15 Control and authentication
$449.43$324.40 +$15 Control and authentication
$354.82$332.29 +$15 Control and authentication
$281.60 +$15 Control and authentication
$168.96 +$15 Control and authentication
$388.61$360.45 +$15 Control and authentication
$225.28$185.86 +$15 Control and authentication
$625.15 +$15 Control and authentication
$101.38 +$15 Control and authentication
$170.09$144.18 +$15 Control and authentication
$393.11$336.79 +$15 Control and authentication
$382.98$324.40 +$15 Control and authentication
$337.92$309.76 +$15 Control and authentication
$315.39 +$15 Control and authentication
$336.79$247.81 +$15 Control and authentication
$168.96 +$15 Control and authentication
$175.39$155.90 +$15 Control and authentication
$214.02 +$15 Control and authentication
$303$297.37 +$15 Control and authentication
$394.24 +$15 Control and authentication
$321.02$304.13 +$15 Control and authentication
$2,478.08 +$15 Control and authentication
$506.88 +$15 Control and authentication
$280.47 +$15 Control and authentication
$61.95$54.07 +$15 Control and authentication
$495.62 +$15 Control and authentication
$324.80 +$15 Control and authentication
$90.11 +$15 Control and authentication
$179.10 +$15 Control and authentication
$152.06 +$15 Control and authentication
$315.39 +$15 Control and authentication
$562.07$449.43 +$15 Control and authentication
$64.96 +$15 Control and authentication
$351.89 +$15 Control and authentication
$112.64 +$15 Control and authentication
$366.08 +$15 Control and authentication
$394.24$134.04 +$15 Control and authentication
$150 +$15 Control and authentication
$281.60$135.17 +$15 Control and authentication
$152.06$112.64 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$73.22 +$15 Control and authentication
$349.18$315.39 +$15 Control and authentication
$337.92 +$15 Control and authentication
$135.17 +$15 Control and authentication
$281.60 +$15 Control and authentication
$337.92$336.79 +$15 Control and authentication
$529.41$337.92 +$15 Control and authentication
$179.10 +$15 Control and authentication
Sold at $236.54 on November 23, 2022
$292.86$259.07 +$15 Control and authentication
$394.24$382.98 +$15 Control and authentication
$73.22 +$15 Control and authentication
$381.85$300.75 +$15 Control and authentication
$343.55$330.04 +$15 Control and authentication
$202.75 +$15 Control and authentication
$131.79 +$15 Control and authentication
$180.22 +$15 Control and authentication
$419.79$340.06 +$15 Control and authentication
$394.24 +$15 Control and authentication
$142.91 +$15 Control and authentication
$225.28 +$15 Control and authentication
$167.60$141.61 +$15 Control and authentication
$336.79 +$15 Control and authentication
$280.47 +$15 Control and authentication
$131.79$91.24 +$15 Control and authentication
$146.43$105.88 +$15 Control and authentication
$225.28$202.75 +$15 Control and authentication
$405.50$368.33 +$15 Control and authentication
$225.28 +$15 Control and authentication
$270.34$177.97 +$15 Control and authentication
$95.74$84.48 +$15 Control and authentication
$336.79 +$15 Control and authentication
Sold at $227.26 on November 21, 2022
$225.28$197.12 +$15 Control and authentication
$56.32 +$15 Control and authentication
$102.50 +$15 Control and authentication
$95.74$90.11 +$15 Control and authentication
$92.97 +$15 Control and authentication
$281.60$227.53 +$15 Control and authentication
$529.41 +$15 Control and authentication
$439.30 +$15 Control and authentication
$174.15$84.05 +$15 Control and authentication
$101.38$91.24 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$168.96$101.38 +$15 Control and authentication
$236.54 +$15 Control and authentication
$225.28$185.86 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$506.88$456.19 +$15 Control and authentication
$315.39 +$15 Control and authentication
$139.32$74.66 +$15 Control and authentication
$139.32$74.66 +$15 Control and authentication
$50.69$39.42 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$239.06 +$15 Control and authentication
$69.45 +$15 Control and authentication
$506.88$408.88 +$15 Control and authentication
$202.75 +$15 Control and authentication
$991.23 +$15 Control and authentication
$135.17$123.90 +$15 Control and authentication
$168.96$135.17 +$15 Control and authentication
$116.02$101.38 +$15 Control and authentication
$141.93$101.38 +$15 Control and authentication
$139.32$78.45 +$15 Control and authentication
$253.44 +$15 Control and authentication
$362.70$337.92 +$15 Control and authentication
$116.02$101.38 +$15 Control and authentication
$444.93 +$15 Control and authentication
$506.88 +$15 Control and authentication
$631.52$591.66 +$15 Control and authentication
$139.32$74.66 +$15 Control and authentication
$38 +$15 Control and authentication
$337.92$312.01 +$15 Control and authentication
$281.60 +$15 Control and authentication
$168.96 +$15 Control and authentication
$309.76$191.49 +$15 Control and authentication
$366.08$354.82 +$15 Control and authentication
$281.60 +$15 Control and authentication
$129.54$111.51 +$15 Control and authentication
$265.83$182.48 +$15 Control and authentication
$168.96$111.51 +$15 Control and authentication
$363.77$272.83 +$15 Control and authentication
$208.38 +$15 Control and authentication
$337.92 +$15 Control and authentication
$208.38$206.13 +$15 Control and authentication
$225.28 +$15 Control and authentication
$394.24$349.18 +$15 Control and authentication
$675.84 +$15 Control and authentication
$676.18 +$15 Control and authentication
$388.46 +$15 Control and authentication
$233.85 +$15 Control and authentication
$77.43 +$15 Control and authentication
$371.71$354.82 +$15 Control and authentication
$139.32$84.05 +$15 Control and authentication
$168.96$123.90 +$15 Control and authentication
$63.39$57.48 +$15 Control and authentication
$214.02$168.96 +$15 Control and authentication
$619.52 +$15 Control and authentication
$450.56$225.28 +$15 Control and authentication
$214.02 +$15 Control and authentication
$438.17 +$15 Control and authentication
$438.17 +$15 Control and authentication
$214.02 +$15 Control and authentication
$208.38 +$15 Control and authentication
$225.28$214.02 +$15 Control and authentication
$419.49$414.70 +$15 Control and authentication
$250.06 +$15 Control and authentication
$450.56 +$15 Control and authentication
$473.09 +$15 Control and authentication
$304.13 +$15 Control and authentication
$101.38 +$15 Control and authentication
$112.64 +$15 Control and authentication
$101.38 +$15 Control and authentication
$130$95 +$15 Control and authentication
$75$45 +$15 Control and authentication
$450.56 +$15 Control and authentication
$439.30$281.60 +$15 Control and authentication
$309.76$239.92 +$15 Control and authentication
$246.85$222.16 +$15 Control and authentication
$112.64 +$15 Control and authentication
$180.22 +$15 Control and authentication
$150$67 +$15 Control and authentication
$394.24$371.71 +$15 Control and authentication
$449.43$429.16 +$15 Control and authentication
$281.60$225.28 +$15 Control and authentication
$257.95 +$15 Control and authentication
$80$70 +$15 Control and authentication
$101.38 +$15 Control and authentication
$377.34 +$15 Control and authentication
$147.56$75.64 +$15 Control and authentication
$315.39 +$15 Control and authentication
$250.06 +$15 Control and authentication
$91.24$54.07 +$15 Control and authentication
$374.37$230.20 +$15 Control and authentication
$112.64$95.74 +$15 Control and authentication
$157.70$135.17 +$15 Control and authentication
$337.92 +$15 Control and authentication
$166.71 +$15 Control and authentication
$394.24$168.96 +$15 Control and authentication
$100 +$15 Control and authentication
$732.16$595.87 +$15 Control and authentication
$280.47 +$15 Control and authentication
$337.92$325.53 +$15 Control and authentication
$394.24 +$15 Control and authentication
$394.24 +$15 Control and authentication
$202.75 +$15 Control and authentication
$116.93$98.74 +$15 Control and authentication
$349.18$328.91 +$15 Control and authentication
$202.75$201.63 +$15 Control and authentication
$1,215.39$618.39 +$15 Control and authentication
$350$193 +$15 Control and authentication
$129.92$80.55 +$15 Control and authentication
$506.88$477.06 +$15 Control and authentication
$506.88$439.96 +$15 Control and authentication
$180.22$111.51 +$15 Control and authentication
$388.61 +$15 Control and authentication
$101.38 +$15 Control and authentication
Sold at $72.72 on November 18, 2022
$112.64$72.09 +$15 Control and authentication
$202.75$191.49 +$15 Control and authentication
$168.96$73.22 +$15 Control and authentication
$324.40$262.45 +$15 Control and authentication
$337.92 +$15 Control and authentication
$135.17$123.90 +$15 Control and authentication
$349.18$315.39 +$15 Control and authentication
$281.60 +$15 Control and authentication
$549.68 +$15 Control and authentication
$281.60$185.86 +$15 Control and authentication
$461.82$377.34 +$15 Control and authentication
$68.27 +$15 Control and authentication
$197.12$167.83 +$15 Control and authentication
$139.32$74.66 +$15 Control and authentication
$275.97$264.70 +$15 Control and authentication
$321.02 +$15 Control and authentication
$450.79 +$15 Control and authentication
$212.89 +$15 Control and authentication
$180.22 +$15 Control and authentication
$84.48$50.69 +$15 Control and authentication
$101.38$72.09 +$15 Control and authentication
$242.18 +$15 Control and authentication
$163.33$112.64 +$15 Control and authentication
$227.36$194.88 +$15 Control and authentication
$315.39 +$15 Control and authentication
$152.06$116.02 +$15 Control and authentication
$493.69 +$15 Control and authentication
$121.65$79.97 +$15 Control and authentication
$140.80$123.90 +$15 Control and authentication
$321.02$253.44 +$15 Control and authentication
$242.18$225.28 +$15 Control and authentication
$75.47 +$15 Control and authentication
$582.35$575.59 +$15 Control and authentication
$111.51 +$15 Control and authentication
$1,234.23 +$15 Control and authentication
$788.48$321.02 +$15 Control and authentication
$84.48$61.95 +$15 Control and authentication
$76.60$46.18 +$15 Control and authentication
$181.35 +$15 Control and authentication
$506.88$394.24 +$15 Control and authentication
$315.39 +$15 Control and authentication
$304.13$265.83 +$15 Control and authentication
$529.41$473.09 +$15 Control and authentication
$56.32 +$15 Control and authentication
$65.33 +$15 Control and authentication
$255.01 +$15 Control and authentication
$135.17$76.60 +$15 Control and authentication
$149.81 +$15 Control and authentication
$281.60$180.22 +$15 Control and authentication
$139.32$84.05 +$15 Control and authentication
$109.26 +$15 Control and authentication
$394.24$371.71 +$15 Control and authentication
$67.58$46.18 +$15 Control and authentication
$336.79 +$15 Control and authentication
$281.60$263.58 +$15 Control and authentication
$70$54 +$15 Control and authentication
$225.28$113.77 +$15 Control and authentication
$444.93$439.30 +$15 Control and authentication
$84.48 +$15 Control and authentication
$78.85$45.06 +$15 Control and authentication
$415.64$342.43 +$15 Control and authentication
$70 +$15 Control and authentication
$281.60 +$15 Control and authentication
$168.96$108.13 +$15 Control and authentication
$405.50$398.75 +$15 Control and authentication
$422.61 +$15 Control and authentication
$360.45 +$15 Control and authentication
$168.96 +$15 Control and authentication
$202.75 +$15 Control and authentication
$309.76 +$15 Control and authentication
$309.76 +$15 Control and authentication
$67.58$54.07 +$15 Control and authentication
$82.23$54.07 +$15 Control and authentication
$325.53$253.44 +$15 Control and authentication
$957.44$788.48 +$15 Control and authentication
$298.50$229.79 +$15 Control and authentication
$394.24$354.82 +$15 Control and authentication
$129.92$116.93 +$15 Control and authentication
$157.20$124.72 +$15 Control and authentication
$233.85 +$15 Control and authentication
$84.48 +$15 Control and authentication
$304.13$273.72 +$15 Control and authentication
$191.49$139.67 +$15 Control and authentication
$35$29 +$15 Control and authentication
$78.85 +$15 Control and authentication
$394.24 +$15 Control and authentication
$399.87$324.40 +$15 Control and authentication
$215.67 +$15 Control and authentication
$69.22 +$15 Control and authentication
$405.50$381.65 +$15 Control and authentication
$357.28 +$15 Control and authentication
$337.92$168.96 +$15 Control and authentication
$146.43$81.10 +$15 Control and authentication
$224.15 +$15 Control and authentication
$653.31 +$15 Control and authentication
$100.25 +$15 Control and authentication
$270.34 +$15 Control and authentication
$71.46 +$15 Control and authentication
$168.96$100.25 +$15 Control and authentication
$489.06 +$15 Control and authentication
$337.92$219.65 +$15 Control and authentication
$214.02$198.25 +$15 Control and authentication
$120$67 +$15 Control and authentication
$394.24$336.79 +$15 Control and authentication
$388.61$304.13 +$15 Control and authentication
$281.60$270.34 +$15 Control and authentication
$338 +$15 Control and authentication
$198.87 +$15 Control and authentication
$387.48 +$15 Control and authentication
$84.48$81.10 +$15 Control and authentication
$77.95 +$15 Control and authentication
Sold at $85.22 on November 17, 2022
$446.05$439.30 +$15 Control and authentication
$382.98$367.21 +$15 Control and authentication
$336.79$303 +$15 Control and authentication
$123.90 +$15 Control and authentication
$417.89$397.62 +$15 Control and authentication
$321.02$241.05 +$15 Control and authentication
$223.03 +$15 Control and authentication
$495.62$471.96 +$15 Control and authentication
$382.98$270.34 +$15 Control and authentication
$675.84$530.07 +$15 Control and authentication
$326.66 +$15 Control and authentication
$405.50$381.65 +$15 Control and authentication
$378.60$340.74 +$15 Control and authentication
$43.93 +$15 Control and authentication
$337.92$230.91 +$15 Control and authentication
$225.28$209.51 +$15 Control and authentication
$202.75 +$15 Control and authentication
$107.01 +$15 Control and authentication
$139.67 +$15 Control and authentication
$146.43 +$15 Control and authentication
$202.75 +$15 Control and authentication
$675.84$619.52 +$15 Control and authentication
$202.75$112.64 +$15 Control and authentication
$102.50$86.73 +$15 Control and authentication
$270.34$223.03 +$15 Control and authentication
$123.90$103.63 +$15 Control and authentication
$493.05$399.37 +$15 Control and authentication
$157.70 +$15 Control and authentication
$321.02$253.44 +$15 Control and authentication
$337.92$230.91 +$15 Control and authentication
$450.56 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$404.38$399.62 +$15 Control and authentication
$619.52 +$15 Control and authentication
$156.57 +$15 Control and authentication
$415.64$391.19 +$15 Control and authentication
$225.28$191.49 +$15 Control and authentication
$450.56$303 +$15 Control and authentication
$321.02 +$15 Control and authentication
$168.96 +$15 Control and authentication
$388.61$287.23 +$15 Control and authentication
$95.88$91.09 +$15 Control and authentication
$219.65$110.39 +$15 Control and authentication
$281.60$112.64 +$15 Control and authentication
$281.60 +$15 Control and authentication
$143.05$130.66 +$15 Control and authentication
$270.34$174.59 +$15 Control and authentication
$180.22$145.31 +$15 Control and authentication
$107.01$84.48 +$15 Control and authentication
$269.21$259.07 +$15 Control and authentication
$281.60$269.21 +$15 Control and authentication
$428.03$336.79 +$15 Control and authentication
$224.15 +$15 Control and authentication
$349.48 +$15 Control and authentication
$336.79$185.86 +$15 Control and authentication
$103.94 +$15 Control and authentication
$135.17$112.64 +$15 Control and authentication
$72.09 +$15 Control and authentication
$84.48$73.22 +$15 Control and authentication
$439.30 +$15 Control and authentication
$112.64$107.01 +$15 Control and authentication
$264.70$121.65 +$15 Control and authentication
$259.07 +$15 Control and authentication
$281.60$221.90 +$15 Control and authentication
$450.56$428.03 +$15 Control and authentication
$1,351.68 +$15 Control and authentication
$303 +$15 Control and authentication
$188.38$129.92 +$15 Control and authentication
$116.93$97.44 +$15 Control and authentication
$281.60 +$15 Control and authentication
$444.93 +$15 Control and authentication
$66.46$64.20 +$15 Control and authentication
$448.31 +$15 Control and authentication
$247.81$145.31 +$15 Control and authentication
$107.01$84.48 +$15 Control and authentication
$68.27 +$15 Control and authentication
$366.08$298.50 +$15 Control and authentication
$145.31$135.17 +$15 Control and authentication
$394.24$354.82 +$15 Control and authentication
$1,351.68 +$15 Control and authentication
$107.01 +$15 Control and authentication
$277.09 +$15 Control and authentication
$78.85$73.22 +$15 Control and authentication
$394.24 +$15 Control and authentication
$201.82$188.70 +$15 Control and authentication
$176.89 +$15 Control and authentication
$194.88$154.60 +$15 Control and authentication
$236.54$208.38 +$15 Control and authentication
$349.18 +$15 Control and authentication
$275.40$260.19 +$15 Control and authentication
$360.45$326.66 +$15 Control and authentication
$146.43 +$15 Control and authentication
$281.60$247.81 +$15 Control and authentication
$101.38$33.79 +$15 Control and authentication
$473.09 +$15 Control and authentication
$473.09 +$15 Control and authentication
$535.04 +$15 Control and authentication
$528.28$473.09 +$15 Control and authentication
$186.70 +$15 Control and authentication
$257.95$235.42 +$15 Control and authentication
$88.99$79.97 +$15 Control and authentication
$135.17 +$15 Control and authentication
$281.60$259.07 +$15 Control and authentication
$394.24$292.86 +$15 Control and authentication
$336.79 +$15 Control and authentication
$123.90 +$15 Control and authentication
$135.17 +$15 Control and authentication
$521.83$398.95 +$15 Control and authentication
$168.96 +$15 Control and authentication
$101.38 +$15 Control and authentication
$337.92 +$15 Control and authentication
$112.64 +$15 Control and authentication
$281.60$236.54 +$15 Control and authentication
$428.03 +$15 Control and authentication
$65$58 +$15 Control and authentication
$128.62 +$15 Control and authentication
$77.72$43.93 +$15 Control and authentication
$1,013.76$957.44 +$15 Control and authentication
$77.72$65.33 +$15 Control and authentication
$50.69 +$15 Control and authentication
$506.88 +$15 Control and authentication
$304.13 +$15 Control and authentication
$337.92 +$15 Control and authentication
$439.30 +$15 Control and authentication
$135.17$122.78 +$15 Control and authentication
$467.46 +$15 Control and authentication
$281.60$247.81 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$224.15 +$15 Control and authentication
$314.40$298.81 +$15 Control and authentication
$242.18$153.19 +$15 Control and authentication
$405.50$263.58 +$15 Control and authentication
$84.48 +$15 Control and authentication
$336.79 +$15 Control and authentication
$224.15$179.10 +$15 Control and authentication
$1,299.19$909.43 +$15 Control and authentication
$563.20$162.20 +$15 Control and authentication
$168.96 +$15 Control and authentication
$67.58$61.95 +$15 Control and authentication
$389.76$374.17 +$15 Control and authentication
$326.66$281.60 +$15 Control and authentication
$242.95$235.15 +$15 Control and authentication
$336.79 +$15 Control and authentication
$168.96 +$15 Control and authentication
$506.88$457.32 +$15 Control and authentication
$336.79 +$15 Control and authentication
$247.81 +$15 Control and authentication
$337.92$321.02 +$15 Control and authentication
$360.45$316.52 +$15 Control and authentication
$157.70$148.68 +$15 Control and authentication
$247.81$225.28 +$15 Control and authentication
$326.66$152.06 +$15 Control and authentication
$140.80 +$15 Control and authentication
$107.01$106.01 +$15 Control and authentication
$267.65$165.66 +$15 Control and authentication
$168.96 +$15 Control and authentication
$394.44$352.18 +$15 Control and authentication
$388.61$321.02 +$15 Control and authentication
$236.54 +$15 Control and authentication
$135.17$114.89 +$15 Control and authentication
$675.84$499 +$15 Control and authentication
$93.49 +$15 Control and authentication
$281.60$270.34 +$15 Control and authentication
$247.81 +$15 Control and authentication
$507.13 +$15 Control and authentication
$163.33$152.06 +$15 Control and authentication
$349.18$287.23 +$15 Control and authentication
$50.69$45.06 +$15 Control and authentication
$168.96 +$15 Control and authentication
$122.78 +$15 Control and authentication
$125.03 +$15 Control and authentication
$135.17 +$15 Control and authentication
$214.02 +$15 Control and authentication
$192.61$136.29 +$15 Control and authentication
$123.90 +$15 Control and authentication
$506.88$461.82 +$15 Control and authentication
$332.29 +$15 Control and authentication
$450.56$225.28 +$15 Control and authentication
$182.48 +$15 Control and authentication
$653.31$529.41 +$15 Control and authentication
$321.02$223.03 +$15 Control and authentication
$129.54$95.74 +$15 Control and authentication
$67.58 +$15 Control and authentication
$608.26$428.03 +$15 Control and authentication
$90.11 +$15 Control and authentication
$126.16 +$15 Control and authentication
$281.60 +$15 Control and authentication
$135.17$116.02 +$15 Control and authentication
$50 +$15 Control and authentication
$309.76 +$15 Control and authentication
$220.86 +$15 Control and authentication
$225.28$174.59 +$15 Control and authentication
$461.82$428.03 +$15 Control and authentication
$135.17 +$15 Control and authentication
$77.72$50.69 +$15 Control and authentication
$67.58 +$15 Control and authentication
$163.33 +$15 Control and authentication
$811.01 +$15 Control and authentication
$394.24$164.45 +$15 Control and authentication
$202.75$185.86 +$15 Control and authentication
$324.80$181.89 +$15 Control and authentication
$513.64$481.30 +$15 Control and authentication
$168.89 +$15 Control and authentication
$214.02$201.63 +$15 Control and authentication
$225.28 +$15 Control and authentication
$619.52$540.67 +$15 Control and authentication
$168.96 +$15 Control and authentication
$207.87 +$15 Control and authentication
$135.17 +$15 Control and authentication
$67.58 +$15 Control and authentication
Sold at $52.27 on November 21, 2022
$168.96 +$15 Control and authentication
$405.50$263.58 +$15 Control and authentication
$129.54 +$15 Control and authentication
$101.38 +$15 Control and authentication
$101.38 +$15 Control and authentication
$70.16 +$15 Control and authentication
$281.60$247.81 +$15 Control and authentication
$619.52 +$15 Control and authentication
$1,220 +$15 Control and authentication
$1,013.76$1,002.50 +$15 Control and authentication
$123.90 +$15 Control and authentication
$354.82$313.14 +$15 Control and authentication
$225.28$112.64 +$15 Control and authentication
$287.23 +$15 Control and authentication
$202.75$138.55 +$15 Control and authentication
$549.68 +$15 Control and authentication
$517.02$486.60 +$15 Control and authentication
$90.11$81.10 +$15 Control and authentication
$242.18$225.28 +$15 Control and authentication
$225.28 +$15 Control and authentication
$393.11$336.79 +$15 Control and authentication
$214.37$214.12 +$15 Control and authentication
$281.60 +$15 Control and authentication
$265$172 +$15 Control and authentication
$122.78 +$15 Control and authentication
$264.70$255.36 +$15 Control and authentication
$191.49 +$15 Control and authentication
$162.20 +$15 Control and authentication
$319.49 +$15 Control and authentication
$337.92$131.79 +$15 Control and authentication
$317.64 +$15 Control and authentication
$619.52$201.63 +$15 Control and authentication
$111.51$56.32 +$15 Control and authentication
$180.22 +$15 Control and authentication
$55.19$48.44 +$15 Control and authentication
$349.18$324.40 +$15 Control and authentication
$114.89$82.23 +$15 Control and authentication
$84.48 +$15 Control and authentication
$225.28$181.35 +$15 Control and authentication
$477.29 +$15 Control and authentication
$247.81 +$15 Control and authentication
$185.86$176.84 +$15 Control and authentication
$155.90$146.81 +$15 Control and authentication
$180.22 +$15 Control and authentication
$506.88$495.62 +$15 Control and authentication
$535.04 +$15 Control and authentication
$337.92 +$15 Control and authentication
$461.82 +$15 Control and authentication
$354.21 +$15 Control and authentication
$155.90$109.13 +$15 Control and authentication
$130$110 +$15 Control and authentication
$173.47 +$15 Control and authentication
$321.02$163.33 +$15 Control and authentication
$529.41$315.39 +$15 Control and authentication
$377.34$292.86 +$15 Control and authentication
$450.56 +$15 Control and authentication
$232.56 +$15 Control and authentication
$315.39 +$15 Control and authentication
$549.39$439.23 +$15 Control and authentication
$226.40$177.03 +$15 Control and authentication
$84.48$76.60 +$15 Control and authentication
$337.92$161.08 +$15 Control and authentication
$309.76$253.44 +$15 Control and authentication
$174.59$168.96 +$15 Control and authentication
$195.99 +$15 Control and authentication
$224.15 +$15 Control and authentication
$337.92$305.25 +$15 Control and authentication
$326.66$225.28 +$15 Control and authentication
$157.70 +$15 Control and authentication
$90.11$70.96 +$15 Control and authentication
$382.98$242.18 +$15 Control and authentication
$506.88$428.03 +$15 Control and authentication
$88.35 +$15 Control and authentication
$112.64$57.45 +$15 Control and authentication
$357.28$175.39 +$15 Control and authentication
$281.60 +$15 Control and authentication
$197.12 +$15 Control and authentication
$111.51$68.71 +$15 Control and authentication
$394.24$377.34 +$15 Control and authentication
$130$94 +$15 Control and authentication
$247.81 +$15 Control and authentication
$128.62$110.43 +$15 Control and authentication
$275.97 +$15 Control and authentication
$112.64$87.86 +$15 Control and authentication
$765.95 +$15 Control and authentication
$115.63$51.97 +$15 Control and authentication
$782.85$501.25 +$15 Control and authentication
$370.59$357.07 +$15 Control and authentication
$360.45$287.23 +$15 Control and authentication
$428.73 +$15 Control and authentication
$259.07$180.22 +$15 Control and authentication
$281.60 +$15 Control and authentication
$197.12 +$15 Control and authentication
$366.08$354.82 +$15 Control and authentication
$61.95 +$15 Control and authentication
$901.12$897.74 +$15 Control and authentication
$219.65 +$15 Control and authentication
$281.60 +$15 Control and authentication
$214.02 +$15 Control and authentication
$130$94 +$15 Control and authentication
$81.10$54.07 +$15 Control and authentication
$278.22$250.06 +$15 Control and authentication
$130.66$118.27 +$15 Control and authentication
$450.56$416.77 +$15 Control and authentication
$145.31$73.22 +$15 Control and authentication
$281.60 +$15 Control and authentication
$197.12 +$15 Control and authentication
$112.64 +$15 Control and authentication
$71.46 +$15 Control and authentication
$563.20 +$15 Control and authentication
$298.50 +$15 Control and authentication
$101.38$64.20 +$15 Control and authentication
$360.45 +$15 Control and authentication
$130$94 +$15 Control and authentication
$354.82$321.02 +$15 Control and authentication
$61.95 +$15 Control and authentication
$152.06 +$15 Control and authentication
$292.32 +$15 Control and authentication
$518.14 +$15 Control and authentication
$111.51 +$15 Control and authentication
$281.60$261.32 +$15 Control and authentication
$515.89$461.82 +$15 Control and authentication
$281.60 +$15 Control and authentication
$104.76 +$15 Control and authentication
$90.11$73.22 +$15 Control and authentication
$288.36$287.23 +$15 Control and authentication
$134.04 +$15 Control and authentication
$42.80$38.30 +$15 Control and authentication
$281.60 +$15 Control and authentication
$107.01 +$15 Control and authentication
$473.09 +$15 Control and authentication
$585.73 +$15 Control and authentication
$236.54$214.02 +$15 Control and authentication
$238.80 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$493.69$415.74 +$15 Control and authentication
$316.94$276.86 +$15 Control and authentication
$208.38 +$15 Control and authentication
$281.60 +$15 Control and authentication
$123.90$101.38 +$15 Control and authentication
$180.22 +$15 Control and authentication
$506.88 +$15 Control and authentication
$788.48 +$15 Control and authentication
$157.70$82.23 +$15 Control and authentication
$175.39$90.94 +$15 Control and authentication
$240.35 +$15 Control and authentication
$585.73$551.94 +$15 Control and authentication
$116.93$110.05 +$15 Control and authentication
$366.08$259.07 +$15 Control and authentication
$69.84$50.69 +$15 Control and authentication
$111.51 +$15 Control and authentication
$58.57$57.45 +$15 Control and authentication
$111.51$48.44 +$15 Control and authentication
$493.05$409.65 +$15 Control and authentication
$168.96 +$15 Control and authentication
$168.96$140.80 +$15 Control and authentication
$280.47 +$15 Control and authentication
$551.94$535.04 +$15 Control and authentication
$67.58 +$15 Control and authentication
$337.92 +$15 Control and authentication
$281.60 +$15 Control and authentication
$61.95 +$15 Control and authentication
$202.75$152.06 +$15 Control and authentication
$326.66$180.96 +$15 Control and authentication
$337.92$95.74 +$15 Control and authentication
$56.32$39.42 +$15 Control and authentication
$168.96$123.90 +$15 Control and authentication
$168.96 +$15 Control and authentication
$47.31$43.93 +$15 Control and authentication
$405.50 +$15 Control and authentication
$103.94 +$15 Control and authentication
$152.06$112.64 +$15 Control and authentication
$225.28$127.28 +$15 Control and authentication
$107.01$101.38 +$15 Control and authentication
$73.22 +$15 Control and authentication
$138.55 +$15 Control and authentication
$281.60$180.22 +$15 Control and authentication
$129.54 +$15 Control and authentication
$157.70 +$15 Control and authentication
$202.75$149.81 +$15 Control and authentication
$270.34$260.79 +$15 Control and authentication
$230.91$229.79 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$129.54 +$15 Control and authentication
$117.15 +$15 Control and authentication
$271.46$188.11 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$389.76$259.84 +$15 Control and authentication
$765.95 +$15 Control and authentication
$107.01$101.38 +$15 Control and authentication
$84.48$68.71 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$64.96$44.17 +$15 Control and authentication
$64.96$44.17 +$15 Control and authentication
$103.94 +$15 Control and authentication
$901.12 +$15 Control and authentication
$50.69 +$15 Control and authentication
$149.41 +$15 Control and authentication
$416.77$281.60 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$405.50 +$15 Control and authentication
$168.96 +$15 Control and authentication
$247.81$244.89 +$15 Control and authentication
$281.60 +$15 Control and authentication
$140.80$129.54 +$15 Control and authentication
$354.82$298.50 +$15 Control and authentication
$76.60$73.22 +$15 Control and authentication
$180.22 +$15 Control and authentication
$449.43 +$15 Control and authentication
$321.02$290.61 +$15 Control and authentication
$104.95 +$15 Control and authentication
$49.56 +$15 Control and authentication
$270.34$201.63 +$15 Control and authentication
$689.36$608.26 +$15 Control and authentication
$388.61$287.23 +$15 Control and authentication
$144.48$111.51 +$15 Control and authentication
$140.80$93.49 +$15 Control and authentication
$103.94$55.87 +$15 Control and authentication
$104.76$103.36 +$15 Control and authentication
$90.11$77.72 +$15 Control and authentication
Sold at $30.41 on November 22, 2022
$309.76$284.25 +$15 Control and authentication
$281.60 +$15 Control and authentication
$658.94 +$15 Control and authentication
$515.89 +$15 Control and authentication
$219.65 +$15 Control and authentication
$321.02 +$15 Control and authentication
$168.96 +$15 Control and authentication
$152.06 +$15 Control and authentication
$388.61$371.71 +$15 Control and authentication
$399.87$259.07 +$15 Control and authentication
$73.22$32.67 +$15 Control and authentication
$394.24$200.50 +$15 Control and authentication
$208.38$111.51 +$15 Control and authentication
$129.54 +$15 Control and authentication
$378.47$377.34 +$15 Control and authentication
$540.67 +$15 Control and authentication
$58.57$52.94 +$15 Control and authentication
$281.60$107.01 +$15 Control and authentication
$152.06$118.27 +$15 Control and authentication
$130$94 +$15 Control and authentication
$130$94 +$15 Control and authentication
$168.96$95.74 +$15 Control and authentication
$84.48$81.10 +$15 Control and authentication
$366.08$336.79 +$15 Control and authentication
$477.59$461.82 +$15 Control and authentication
$493.05$464.87 +$15 Control and authentication
$74.34$67.58 +$15 Control and authentication
$197.12$182.48 +$15 Control and authentication
$302.28$294.33 +$15 Control and authentication
$95.74 +$15 Control and authentication
$405.50$262.45 +$15 Control and authentication
$84.48$61.95 +$15 Control and authentication
$77.72$69.84 +$15 Control and authentication
$506.88$495.62 +$15 Control and authentication
$135.17 +$15 Control and authentication
$116.02$110.39 +$15 Control and authentication
$563.20 +$15 Control and authentication
$318.19 +$15 Control and authentication
$190.36$145.31 +$15 Control and authentication
$563.20$535.04 +$15 Control and authentication
Sold at $274.83 on November 21, 2022
$69.84$56.32 +$15 Control and authentication
$61.95 +$15 Control and authentication
$394.24 +$15 Control and authentication
$281.60$191.49 +$15 Control and authentication
$129.54 +$15 Control and authentication
$168.96$56.32 +$15 Control and authentication
$219.65$185.86 +$15 Control and authentication
$506.88 +$15 Control and authentication
$247.81$200.50 +$15 Control and authentication
$33.79 +$15 Control and authentication
$95.74$64.20 +$15 Control and authentication
$168.96 +$15 Control and authentication
$450.56$337.92 +$15 Control and authentication
$140.80 +$15 Control and authentication
$957.44 +$15 Control and authentication
$180.22 +$15 Control and authentication
$90.94$55.87 +$15 Control and authentication
$202.75 +$15 Control and authentication
$78.85$42.80 +$15 Control and authentication
$32.67$28.16 +$15 Control and authentication
$157.70 +$15 Control and authentication
$129.54 +$15 Control and authentication
$212.89$190.36 +$15 Control and authentication
$112.64 +$15 Control and authentication
$394.24 +$15 Control and authentication
$121.65 +$15 Control and authentication
$202.75$123.90 +$15 Control and authentication
$281.60 +$15 Control and authentication
$191.49$163.33 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$540.67 +$15 Control and authentication
$1,239.66$560.66 +$15 Control and authentication
$129.54 +$15 Control and authentication
$335.27 +$15 Control and authentication
$84.48 +$15 Control and authentication
$111.51$100.25 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$645.29 +$15 Control and authentication
$168.96 +$15 Control and authentication
$129.54 +$15 Control and authentication
$191.49 +$15 Control and authentication
$39.42 +$15 Control and authentication
$326.66$282.73 +$15 Control and authentication
$78.85$69.84 +$15 Control and authentication
$281.60 +$15 Control and authentication
$110.39 +$15 Control and authentication
$247.81$119.40 +$15 Control and authentication
$957.44$930.41 +$15 Control and authentication
$535.31 +$15 Control and authentication
$2,703.36$1,689.60 +$15 Control and authentication
$95.74 +$15 Control and authentication
$285.54 +$15 Control and authentication
$64.96$63.66 +$15 Control and authentication
$399.87$398.75 +$15 Control and authentication
$281.60$268.35 +$15 Control and authentication
$110.39$101.38 +$15 Control and authentication
$101.38$83.35 +$15 Control and authentication
$315.39 +$15 Control and authentication
$84.48$73.22 +$15 Control and authentication
$382.98$304.13 +$15 Control and authentication
$130$110 +$15 Control and authentication
$39.42$33.79 +$15 Control and authentication
$901.12 +$15 Control and authentication
$202.75$147.56 +$15 Control and authentication
$112.64 +$15 Control and authentication
$228$199 +$15 Control and authentication
$405.50$214.02 +$15 Control and authentication
$399.87$197.12 +$15 Control and authentication
$112.64 +$15 Control and authentication
$281.60 +$15 Control and authentication
$202.75$191.49 +$15 Control and authentication
$450.79 +$15 Control and authentication
$506.88 +$15 Control and authentication
$223.03 +$15 Control and authentication
$61.95$50.69 +$15 Control and authentication
$323.50$268.93 +$15 Control and authentication
$563.20$397.62 +$15 Control and authentication
$168.96$111.51 +$15 Control and authentication
$84.48 +$15 Control and authentication
$355.98 +$15 Control and authentication
$74.66$62.41 +$15 Control and authentication
$253.44$225.28 +$15 Control and authentication
$449.43 +$15 Control and authentication
$518.14$304.13 +$15 Control and authentication
$377.34$292.86 +$15 Control and authentication
$1,351.68$966.45 +$15 Control and authentication
$78.85 +$15 Control and authentication
$168.96$157.70 +$15 Control and authentication
$129.54 +$15 Control and authentication
$90.11$61.95 +$15 Control and authentication
$280.47$269.21 +$15 Control and authentication
$85.75 +$15 Control and authentication
$108.13 +$15 Control and authentication
$405.50$399.87 +$15 Control and authentication
$202.75$135.17 +$15 Control and authentication
$168.96$163.33 +$15 Control and authentication
$84.48 +$15 Control and authentication
$77.95$37.68 +$15 Control and authentication
$100.25$46.18 +$15 Control and authentication
$687.10$422.40 +$15 Control and authentication
$247.81$197.12 +$15 Control and authentication
$232.04 +$15 Control and authentication
$112.64$103.63 +$15 Control and authentication
$324.80$298.81 +$15 Control and authentication
$95.88 +$15 Control and authentication
$393.11$300.75 +$15 Control and authentication
$298.54 +$15 Control and authentication
$225.28$168.96 +$15 Control and authentication
$275.97$225.28 +$15 Control and authentication
$180.22 +$15 Control and authentication
$440 +$15 Control and authentication
$214.02$137.42 +$15 Control and authentication
$500.12$484.35 +$15 Control and authentication
$107.01$106.01 +$15 Control and authentication
$214.02$180.22 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$300.75$257.95 +$15 Control and authentication
$732.16$675.84 +$15 Control and authentication
$540.67 +$15 Control and authentication
$428.03 +$15 Control and authentication
$428.03 +$15 Control and authentication
$123.90 +$15 Control and authentication
$281.60 +$15 Control and authentication
$52.94 +$15 Control and authentication
$963.07$794.11 +$15 Control and authentication
$1,013.76$957.44 +$15 Control and authentication
$318.30 +$15 Control and authentication
$225.28$180.22 +$15 Control and authentication
$416.77$360.45 +$15 Control and authentication
$77.95$37.68 +$15 Control and authentication
$318.30 +$15 Control and authentication
$95.88 +$15 Control and authentication
$563.20$529.41 +$15 Control and authentication
$363.77 +$15 Control and authentication
$360.45$348.06 +$15 Control and authentication
$491.52$409.60 +$15 Control and authentication
$168.96$87.86 +$15 Control and authentication
$130$94 +$15 Control and authentication
$324.80$292.32 +$15 Control and authentication
$337.92 +$15 Control and authentication
$116.93$24.68 +$15 Control and authentication
$247.81$191.49 +$15 Control and authentication
$84.48$73.22 +$15 Control and authentication
$618.39$314.27 +$15 Control and authentication
$40 +$15 Control and authentication
$411.14 +$15 Control and authentication
$168.96 +$15 Control and authentication
$281.60$199.37 +$15 Control and authentication
$540.67 +$15 Control and authentication
$326.66$223.03 +$15 Control and authentication
$225.28$191.49 +$15 Control and authentication
$619.52 +$15 Control and authentication
$111.51$92.36 +$15 Control and authentication
$95.74$52.94 +$15 Control and authentication
$264.70 +$15 Control and authentication
$154.96 +$15 Control and authentication
$281.60$224.15 +$15 Control and authentication
$130$90 +$15 Control and authentication
$101.38 +$15 Control and authentication
$394.24 +$15 Control and authentication
$225.28 +$15 Control and authentication
$450.56$225.28 +$15 Control and authentication
$247.81$236.54 +$15 Control and authentication
$332.29 +$15 Control and authentication
$97.44$84.45 +$15 Control and authentication
$112.64$57.45 +$15 Control and authentication
$714.56$708.06 +$15 Control and authentication
$337.92 +$15 Control and authentication
$168.96$157.70 +$15 Control and authentication
$107.01$86.73 +$15 Control and authentication
$354.82$236.54 +$15 Control and authentication
$207.87 +$15 Control and authentication
$182.48$164.45 +$15 Control and authentication
$394.24$309.76 +$15 Control and authentication
$85.75 +$15 Control and authentication
$77.72 +$15 Control and authentication
$337.92 +$15 Control and authentication
$111.51 +$15 Control and authentication
$332.29$168.96 +$15 Control and authentication
$225.28$223.03 +$15 Control and authentication
$245.55$167.60 +$15 Control and authentication
$155.90$103.94 +$15 Control and authentication
$225.28$139.67 +$15 Control and authentication
$281.60 +$15 Control and authentication
$201.63$171.21 +$15 Control and authentication
$140.80 +$15 Control and authentication
$122.78 +$15 Control and authentication
$169$149 +$15 Control and authentication
$259.84$214.37 +$15 Control and authentication
$704.35 +$15 Control and authentication
$354.82$281.60 +$15 Control and authentication
$280.47$190.36 +$15 Control and authentication
$142.91$136.42 +$15 Control and authentication
$149.41$142.91 +$15 Control and authentication
$304.13$117.15 +$15 Control and authentication
$163.33 +$15 Control and authentication
$129.54 +$15 Control and authentication
$315.39 +$15 Control and authentication
$73.22$63.08 +$15 Control and authentication
$194.88 +$15 Control and authentication
$830 +$15 Control and authentication
$371.71$309.76 +$15 Control and authentication
$337.92$315.39 +$15 Control and authentication
$129.92$49.37 +$15 Control and authentication
$394.24$259.07 +$15 Control and authentication
$212.89 +$15 Control and authentication
$155.90$90.94 +$15 Control and authentication
$123.90 +$15 Control and authentication
$168.96$111.51 +$15 Control and authentication
$50.69 +$15 Control and authentication
$326.66 +$15 Control and authentication
$333.41$332.29 +$15 Control and authentication
$337.92 +$15 Control and authentication
$146.43$129.54 +$15 Control and authentication
$670.21$450.56 +$15 Control and authentication
$95.74 +$15 Control and authentication
$152.06 +$15 Control and authentication
$281.60$247.81 +$15 Control and authentication
$69.89 +$15 Control and authentication
$315.39$281.60 +$15 Control and authentication
$999 +$15 Control and authentication
$416.77$236.54 +$15 Control and authentication
$287.23$252.31 +$15 Control and authentication
$225.28 +$15 Control and authentication
$326.66 +$15 Control and authentication
$259.07$202.75 +$15 Control and authentication
$135.17 +$15 Control and authentication
$281.60$180.22 +$15 Control and authentication
$130$94 +$15 Control and authentication
$139.32$74.66 +$15 Control and authentication
$139.32$74.66 +$15 Control and authentication
$95.74$30.41 +$15 Control and authentication
$129.54$112.64 +$15 Control and authentication
$225.28 +$15 Control and authentication
$343.55$281.60 +$15 Control and authentication
$168.96 +$15 Control and authentication
$130$94 +$15 Control and authentication
$337.92 +$15 Control and authentication
$67.58$56.32 +$15 Control and authentication
$130$95 +$15 Control and authentication
$337.92 +$15 Control and authentication
$337.92$242.18 +$15 Control and authentication
$428.03 +$15 Control and authentication
$224.15$108.13 +$15 Control and authentication
$90.11$81.10 +$15 Control and authentication
$219.65 +$15 Control and authentication
$88.99$48.44 +$15 Control and authentication
$214.37$72.75 +$15 Control and authentication
$130$95 +$15 Control and authentication
$141.93$98 +$15 Control and authentication
$315.39$238.80 +$15 Control and authentication
$168.96 +$15 Control and authentication
$103.94$102.64 +$15 Control and authentication
$450.56$253.44 +$15 Control and authentication
$444.93$263.58 +$15 Control and authentication
$64.20$28.16 +$15 Control and authentication
$112.64$78.85 +$15 Control and authentication
$303 +$15 Control and authentication
$111.51$92.76 +$15 Control and authentication
$280.47$263.58 +$15 Control and authentication
$96.87$86.73 +$15 Control and authentication
$615 +$15 Control and authentication
$394.24$315.39 +$15 Control and authentication
$168.96 +$15 Control and authentication
$101.38$99.39 +$15 Control and authentication
$270.34$242.18 +$15 Control and authentication
$194.88$129.92 +$15 Control and authentication
$168.96 +$15 Control and authentication
$63.66 +$15 Control and authentication
$366.08$275.97 +$15 Control and authentication
$123.90$95.74 +$15 Control and authentication
$405.50$382.98 +$15 Control and authentication
$84.48$49.56 +$15 Control and authentication
$84.48$81.10 +$15 Control and authentication
$180.22 +$15 Control and authentication
$326.66 +$15 Control and authentication
$43.15$27.57 +$15 Control and authentication
$55.19 +$15 Control and authentication
$246.68$171.38 +$15 Control and authentication
$168.96$163.33 +$15 Control and authentication
$219.65$218.52 +$15 Control and authentication
$140.80 +$15 Control and authentication
$506.88 +$15 Control and authentication
$67.58$42.80 +$15 Control and authentication
$224.15 +$15 Control and authentication
$84.48$64.20 +$15 Control and authentication
$130$94 +$15 Control and authentication
$163.33$114.89 +$15 Control and authentication
$450$169 +$15 Control and authentication
$366.08 +$15 Control and authentication
$428.03 +$15 Control and authentication
$130$95 +$15 Control and authentication
$131.84$118.18 +$15 Control and authentication
$327.87$291.44 +$15 Control and authentication
$61.95 +$15 Control and authentication
$838 +$15 Control and authentication
$838 +$15 Control and authentication
$112.64 +$15 Control and authentication
$315.39$281.60 +$15 Control and authentication
$112.64$86.73 +$15 Control and authentication
$1,013.76$562.07 +$15 Control and authentication
$444.93 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$84.48$81.10 +$15 Control and authentication
$620.47$617.29 +$15 Control and authentication
$1,115.14 +$15 Control and authentication
Sold at $166.66 on November 21, 2022
$141.93 +$15 Control and authentication
$433.66$208.38 +$15 Control and authentication
$168.96$140.80 +$15 Control and authentication
$597.63$467.71 +$15 Control and authentication
$214.02 +$15 Control and authentication
$168.96$112.64 +$15 Control and authentication
$292.86$281.60 +$15 Control and authentication
$361.57 +$15 Control and authentication
$224.15$214.02 +$15 Control and authentication
$129.92 +$15 Control and authentication
$129.54$90.11 +$15 Control and authentication
$78.85 +$15 Control and authentication
$999 +$15 Control and authentication
$191.49 +$15 Control and authentication
$360.45$225.28 +$15 Control and authentication
$200.50$185.86 +$15 Control and authentication
$337.92$225.28 +$15 Control and authentication
$109.13$85.75 +$15 Control and authentication
$146.43$123.90 +$15 Control and authentication
$315.39 +$15 Control and authentication
$135.17 +$15 Control and authentication
$175.39$116.93 +$15 Control and authentication
$77.95$71.46 +$15 Control and authentication
$45.47$43.45 +$15 Control and authentication
$208.38 +$15 Control and authentication
$270.34 +$15 Control and authentication
$676.18$591.66 +$15 Control and authentication
$65.33$36.04 +$15 Control and authentication
$674.71$595.34 +$15 Control and authentication
$225.28 +$15 Control and authentication
$428.03$335.67 +$15 Control and authentication
$359.32$211.76 +$15 Control and authentication
$360.45 +$15 Control and authentication
$354.82$253.44 +$15 Control and authentication
$343.55$270.34 +$15 Control and authentication
$225.28$139.67 +$15 Control and authentication
$130$110 +$15 Control and authentication
$217.40 +$15 Control and authentication
$84.45$37.68 +$15 Control and authentication
$225.28$214.02 +$15 Control and authentication
$224.15 +$15 Control and authentication
$214.02$191.49 +$15 Control and authentication
$168.96 +$15 Control and authentication
$259.07 +$15 Control and authentication
$146.43 +$15 Control and authentication
$78.85 +$15 Control and authentication
$122.78 +$15 Control and authentication
$167.83 +$15 Control and authentication
$336.79$253.44 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$190.36$162.20 +$15 Control and authentication
$180.22 +$15 Control and authentication
$180.22 +$15 Control and authentication
$103.94$46.77 +$15 Control and authentication
$354.82$270.34 +$15 Control and authentication
Sold at $45 on November 23, 2022
$73.22$42.80 +$15 Control and authentication
$289 +$15 Control and authentication
$242.18 +$15 Control and authentication
$123.42$45.47 +$15 Control and authentication
$84.48 +$15 Control and authentication
$156.57$104.76 +$15 Control and authentication
$78.85$75.47 +$15 Control and authentication
$96.87$86.73 +$15 Control and authentication
$112.64$101.38 +$15 Control and authentication
$326.66$168.96 +$15 Control and authentication
$439.30 +$15 Control and authentication
$354.82$304.13 +$15 Control and authentication
$376.22$225.28 +$15 Control and authentication
$157.70$145.31 +$15 Control and authentication
$281.60$225.28 +$15 Control and authentication
$303 +$15 Control and authentication
$337.92 +$15 Control and authentication
$77.72$69.84 +$15 Control and authentication
$129.54$111.31 +$15 Control and authentication
$56.32$45.06 +$15 Control and authentication
$428.03 +$15 Control and authentication
$225.28$184.73 +$15 Control and authentication
$56.32 +$15 Control and authentication
$107.01 +$15 Control and authentication
$225.28 +$15 Control and authentication
$337.92 +$15 Control and authentication
$428.03$394.24 +$15 Control and authentication
$166.23$152.99 +$15 Control and authentication
$67.58 +$15 Control and authentication
$1,112.88 +$15 Control and authentication
$140.80 +$15 Control and authentication
$465 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$112.64 +$15 Control and authentication
$335.67$292.86 +$15 Control and authentication
$281.60$174.59 +$15 Control and authentication
$901.12 +$15 Control and authentication
$350$348 +$15 Control and authentication
$399 +$15 Control and authentication
Sold at $405.50 on November 23, 2022
$500.09$377.53 +$15 Control and authentication
Sold at $495.62 on November 22, 2022
$135.17$90.11 +$15 Control and authentication
$112.64$93.49 +$15 Control and authentication
$389.76$255.94 +$15 Control and authentication
$100.25$90.11 +$15 Control and authentication
$54.07 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$2,027.52$1,745.92 +$15 Control and authentication
$130$99 +$15 Control and authentication
$156.51 +$15 Control and authentication
$109.26$92.36 +$15 Control and authentication
$483.23 +$15 Control and authentication
$191.49$163.33 +$15 Control and authentication
$110.39$63.08 +$15 Control and authentication
$225.28 +$15 Control and authentication
$281.60$251.19 +$15 Control and authentication
$279.35 +$15 Control and authentication
$122.78 +$15 Control and authentication
$106.02$90.11 +$15 Control and authentication
$546.30$506.88 +$15 Control and authentication
$439.30 +$15 Control and authentication
$450.56 +$15 Control and authentication
$336.79$324.40 +$15 Control and authentication
$157.70 +$15 Control and authentication
$101.38$84.48 +$15 Control and authentication
$182.48$52.94 +$15 Control and authentication
$585.73$542.92 +$15 Control and authentication
$170.17 +$15 Control and authentication
$145.31 +$15 Control and authentication
$157.70 +$15 Control and authentication
$540.67 +$15 Control and authentication
$95.74$66.46 +$15 Control and authentication
$104.24 +$15 Control and authentication
$281.60$206.13 +$15 Control and authentication
$394.24 +$15 Control and authentication
$188.38$162.40 +$15 Control and authentication
$167.83 +$15 Control and authentication
$397.74$396.94 +$15 Control and authentication
$214.02$143.05 +$15 Control and authentication
$382.36$308.87 +$15 Control and authentication
$298.50$201.63 +$15 Control and authentication
$281.60$253.44 +$15 Control and authentication
$56.32$45.06 +$15 Control and authentication
$168.89$155.90 +$15 Control and authentication
$168.89$162.40 +$15 Control and authentication
$202.75 +$15 Control and authentication
$506.88 +$15 Control and authentication
$1,068.95$660.07 +$15 Control and authentication
$101.38 +$15 Control and authentication
$518.14 +$15 Control and authentication
$292.86$259.07 +$15 Control and authentication
$168.96 +$15 Control and authentication
$428.03$281.60 +$15 Control and authentication
$276.04 +$15 Control and authentication
$202.75$146.43 +$15 Control and authentication
$247.81 +$15 Control and authentication
$168.89$162.40 +$15 Control and authentication
$191.49 +$15 Control and authentication
$450.79 +$15 Control and authentication
$180.22 +$15 Control and authentication
$332.29$253.44 +$15 Control and authentication
$321.02$259.07 +$15 Control and authentication
$212.89$191.49 +$15 Control and authentication
$563.20$292.86 +$15 Control and authentication
$107.63 +$15 Control and authentication
$2,403.51$2,182.64 +$15 Control and authentication
$168.96 +$15 Control and authentication
$84.48$81.10 +$15 Control and authentication
$630.11 +$15 Control and authentication
$371.71$326.66 +$15 Control and authentication
$506.88$444.93 +$15 Control and authentication
$168.96 +$15 Control and authentication
$264.70 +$15 Control and authentication
$168.96$140.80 +$15 Control and authentication
Sold at $284.08 on November 15, 2022
$61.95$33.79 +$15 Control and authentication
$315.39$287.23 +$15 Control and authentication
$112.64$92.76 +$15 Control and authentication
$416.77 +$15 Control and authentication
$263.58 +$15 Control and authentication
$338 +$15 Control and authentication
$118.27$79.97 +$15 Control and authentication
$59.76 +$15 Control and authentication
$957.44$788.48 +$15 Control and authentication
$326.66$225.28 +$15 Control and authentication
$112.64$67.58 +$15 Control and authentication
$225.28$88.99 +$15 Control and authentication
$225.28 +$15 Control and authentication
$86.73$63.08 +$15 Control and authentication
$129.54 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$168.96$111.51 +$15 Control and authentication
$449.43 +$15 Control and authentication
$444.93$439.30 +$15 Control and authentication
$168.89$155.90 +$15 Control and authentication
$260.20 +$15 Control and authentication
$309.76$239.92 +$15 Control and authentication
$103.94$97.44 +$15 Control and authentication
$197.24$171.70 +$15 Control and authentication
$450.56 +$15 Control and authentication
$100 +$15 Control and authentication
$1,012.63$867.33 +$15 Control and authentication
$394.24$309.76 +$15 Control and authentication
$202.75$168.96 +$15 Control and authentication
$259.07 +$15 Control and authentication
$337.92 +$15 Control and authentication
$123.90$98 +$15 Control and authentication
$260.20$247.81 +$15 Control and authentication
$416.77 +$15 Control and authentication
$152.06$140.80 +$15 Control and authentication
$439.30$146.43 +$15 Control and authentication
$461.82 +$15 Control and authentication
$130$110 +$15 Control and authentication
$123.90$107.01 +$15 Control and authentication
$1,351.68 +$15 Control and authentication
$90.11$86.73 +$15 Control and authentication
Sold at $233.11 on November 23, 2022
$202.75$123.90 +$15 Control and authentication
$202.75$112.64 +$15 Control and authentication
$675.84$674.71 +$15 Control and authentication
$437.04 +$15 Control and authentication
$68.71$50.69 +$15 Control and authentication
$202.75$172.34 +$15 Control and authentication
$270.34$205 +$15 Control and authentication
$545.66 +$15 Control and authentication
$134.04$74.34 +$15 Control and authentication
$506.88$457.32 +$15 Control and authentication
$135.17$90.11 +$15 Control and authentication
$439.30 +$15 Control and authentication
$259.07$221.90 +$15 Control and authentication
$450.56$246.68 +$15 Control and authentication
$394.24$313.14 +$15 Control and authentication
$225.28 +$15 Control and authentication
$109.08$90.71 +$15 Control and authentication
$179.10 +$15 Control and authentication
$211.31$198.63 +$15 Control and authentication
$675.84 +$15 Control and authentication
$382.98 +$15 Control and authentication
$247.81$211.76 +$15 Control and authentication
$642.05 +$15 Control and authentication
$112.64 +$15 Control and authentication
$202.75$182.48 +$15 Control and authentication
$281.60 +$15 Control and authentication
$335.67$326.66 +$15 Control and authentication
$675.84 +$15 Control and authentication
$352.18 +$15 Control and authentication
$56.32 +$15 Control and authentication
$56.32 +$15 Control and authentication
$56.32 +$15 Control and authentication
$56.32 +$15 Control and authentication
$56.32 +$15 Control and authentication
$121.65$84.48 +$15 Control and authentication
$336.79 +$15 Control and authentication
$112.64$78.85 +$15 Control and authentication
$281.60$268.35 +$15 Control and authentication
$199.37$145.31 +$15 Control and authentication
$366.26 +$15 Control and authentication
$360.45$216.27 +$15 Control and authentication
$180$78 +$15 Control and authentication
$394.24 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$123.90 +$15 Control and authentication
$732.53 +$15 Control and authentication
$957.44 +$15 Control and authentication
$428.03$371.71 +$15 Control and authentication
$357.28$344.29 +$15 Control and authentication
$107.01$95.74 +$15 Control and authentication
$129.54 +$15 Control and authentication
$50.69 +$15 Control and authentication
$135.17$112.64 +$15 Control and authentication
$563.20$275.97 +$15 Control and authentication
$1,103.87$833.54 +$15 Control and authentication
$337.92$262.38 +$15 Control and authentication
$112.64 +$15 Control and authentication
$100.44$72.87 +$15 Control and authentication
$148.68$120.52 +$15 Control and authentication
$224.15$208.38 +$15 Control and authentication
$233.85$194.88 +$15 Control and authentication
$473.09 +$15 Control and authentication
$224.15$174.59 +$15 Control and authentication
$878.59 +$15 Control and authentication
$78.85$75.47 +$15 Control and authentication
$84.45$83.15 +$15 Control and authentication
$281.60 +$15 Control and authentication
$103.94$74.56 +$15 Control and authentication
$66.46 +$15 Control and authentication
$292.86 +$15 Control and authentication
$79.55 +$15 Control and authentication
$144.99$134.79 +$15 Control and authentication
$428.03 +$15 Control and authentication
$349.18$308.10 +$15 Control and authentication
$515 +$15 Control and authentication
$304.13$57.45 +$15 Control and authentication
$331.83$320.35 +$15 Control and authentication
$270.34 +$15 Control and authentication
$72.09 +$15 Control and authentication
$500.09$391.62 +$15 Control and authentication
$500.09$391.62 +$15 Control and authentication
$337.92$319.90 +$15 Control and authentication
$90.94 +$15 Control and authentication
$439.30 +$15 Control and authentication
$48.44 +$15 Control and authentication
$77.95$51.97 +$15 Control and authentication
$152.06 +$15 Control and authentication
$225.28$156.57 +$15 Control and authentication
$101.38$45.06 +$15 Control and authentication
$225.28 +$15 Control and authentication
$838 +$15 Control and authentication
$332.29$309.76 +$15 Control and authentication
$73.22 +$15 Control and authentication
$731.03 +$15 Control and authentication
$394.24 +$15 Control and authentication
$247.81$157.70 +$15 Control and authentication
$596.61 +$15 Control and authentication
$991.23$957.44 +$15 Control and authentication
$88.35$37.68 +$15 Control and authentication
$500.09$394.44 +$15 Control and authentication
$500.09$394.44 +$15 Control and authentication
$130$110 +$15 Control and authentication
$191.49 +$15 Control and authentication
$630.78 +$15 Control and authentication
$584.64 +$15 Control and authentication
$360.45 +$15 Control and authentication
$412.26 +$15 Control and authentication
$844.48$733.66 +$15 Control and authentication
$251.19 +$15 Control and authentication
$315.39$268.35 +$15 Control and authentication
$692.74 +$15 Control and authentication
$140.80$75.47 +$15 Control and authentication
$142.91 +$15 Control and authentication
$252.61$155.01 +$15 Control and authentication
$56.32$39.42 +$15 Control and authentication
$73.22$50.69 +$15 Control and authentication
$200$135 +$15 Control and authentication
$84.48$54.07 +$15 Control and authentication
$318.19 +$15 Control and authentication
$77.72 +$15 Control and authentication
$428.03$405.50 +$15 Control and authentication
$194.88$100.04 +$15 Control and authentication
$298.50$269.21 +$15 Control and authentication
$332.29$321.02 +$15 Control and authentication
$250.06$190.36 +$15 Control and authentication
$130$94 +$15 Control and authentication
$219.65$214.02 +$15 Control and authentication
$545.66$454.72 +$15 Control and authentication
$78.85 +$15 Control and authentication
$281.60$252.98 +$15 Control and authentication
$163.33 +$15 Control and authentication
$162.20$135.17 +$15 Control and authentication
$191.49 +$15 Control and authentication
$153.19 +$15 Control and authentication
$197.12 +$15 Control and authentication
$337.92$146.43 +$15 Control and authentication
$168.96 +$15 Control and authentication
$121.65$112.64 +$15 Control and authentication
$167.83$92.36 +$15 Control and authentication
$506.88 +$15 Control and authentication
$101.38$55.19 +$15 Control and authentication
$88.99$56.32 +$15 Control and authentication
$281.60$220.77 +$15 Control and authentication
$90.11 +$15 Control and authentication
$253.44$82.23 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$454.72 +$15 Control and authentication
$450.56 +$15 Control and authentication
$95.74 +$15 Control and authentication
$211.31 +$15 Control and authentication
$101.38$66.46 +$15 Control and authentication
$336.79 +$15 Control and authentication
$281.60$253.44 +$15 Control and authentication
$65.33$50.69 +$15 Control and authentication
$394.24$371.71 +$15 Control and authentication
$336.79 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$280$259 +$15 Control and authentication
$55.19 +$15 Control and authentication
$281.60$135.17 +$15 Control and authentication
$117.15 +$15 Control and authentication
$190.36 +$15 Control and authentication
$506.88$450.56 +$15 Control and authentication
Sold at $136.36 on November 21, 2022
$202.75$168.96 +$15 Control and authentication
$428.03 +$15 Control and authentication
$332.29 +$15 Control and authentication
$315.39 +$15 Control and authentication
$103.94 +$15 Control and authentication
$698.37 +$15 Control and authentication
$437.51$429.56 +$15 Control and authentication
$168.96$129.54 +$15 Control and authentication
$631.52 +$15 Control and authentication
$215.74$210.95 +$15 Control and authentication
$214.02 +$15 Control and authentication
$484.35$461.82 +$15 Control and authentication
$337.92$315.39 +$15 Control and authentication
$71.46$28.58 +$15 Control and authentication
$253.44 +$15 Control and authentication
$253.44 +$15 Control and authentication
$466.41$388.46 +$15 Control and authentication
$72$41 +$15 Control and authentication
$225.28$129.54 +$15 Control and authentication
$354.82 +$15 Control and authentication
$111.51 +$15 Control and authentication
$444.93$439.30 +$15 Control and authentication
$450.56$428.03 +$15 Control and authentication
$95.74$92.76 +$15 Control and authentication
$211.31$169.04 +$15 Control and authentication
$84.48$73.22 +$15 Control and authentication
$61.95$41.68 +$15 Control and authentication
$168.96$135.17 +$15 Control and authentication
$185.86$135.17 +$15 Control and authentication
$251.19 +$15 Control and authentication
$163.33$134.04 +$15 Control and authentication
$58.46 +$15 Control and authentication
$135.17 +$15 Control and authentication
Sold at $200 on November 17, 2022
$563.20$450.56 +$15 Control and authentication
$130$95 +$15 Control and authentication
$110$64 +$15 Control and authentication
$500.09$408.52 +$15 Control and authentication
$397.74 +$15 Control and authentication
$95.74 +$15 Control and authentication
$429.16 +$15 Control and authentication
$281.60$257.95 +$15 Control and authentication
$968.70$957.44 +$15 Control and authentication
$450.56 +$15 Control and authentication
$50.69$39.42 +$15 Control and authentication
$153.19 +$15 Control and authentication
$394.24$387.48 +$15 Control and authentication
$168.96 +$15 Control and authentication
$191.49 +$15 Control and authentication
$394.24$336.79 +$15 Control and authentication
$331.29 +$15 Control and authentication
$549.68 +$15 Control and authentication
$422.61 +$15 Control and authentication
$278.22 +$15 Control and authentication
$225.28$202.75 +$15 Control and authentication
$562.07 +$15 Control and authentication
$337.92 +$15 Control and authentication
$97.44 +$15 Control and authentication
$545.66$506.69 +$15 Control and authentication
$162.20 +$15 Control and authentication
$130$110 +$15 Control and authentication
$84.45$83.15 +$15 Control and authentication
$77.95$37.68 +$15 Control and authentication
$247.81$236.54 +$15 Control and authentication
$394.24$277.66 +$15 Control and authentication
$428.03$376.22 +$15 Control and authentication
$287.23$153.19 +$15 Control and authentication
$439.30 +$15 Control and authentication
$817.05 +$15 Control and authentication
$309.76$284.25 +$15 Control and authentication
$57.41 +$15 Control and authentication
$57.41 +$15 Control and authentication
$167.83 +$15 Control and authentication
$167.83 +$15 Control and authentication
$264.70 +$15 Control and authentication
$107.01$106.01 +$15 Control and authentication
$298.50$247.81 +$15 Control and authentication
$218.35 +$15 Control and authentication
$563.20 +$15 Control and authentication
$261.32$211.76 +$15 Control and authentication
$405.50$349.18 +$15 Control and authentication
$957.44 +$15 Control and authentication
$202.75$197.12 +$15 Control and authentication
$95.74 +$15 Control and authentication
$129.54 +$15 Control and authentication
$197.12$182.48 +$15 Control and authentication
$145.31 +$15 Control and authentication
$145.31 +$15 Control and authentication
$145.31 +$15 Control and authentication
$145.31 +$15 Control and authentication
$145.31 +$15 Control and authentication
$95.74$92.76 +$15 Control and authentication
$999 +$15 Control and authentication
$999 +$15 Control and authentication
$337.92 +$15 Control and authentication
$1,098.24 +$15 Control and authentication
$551.94 +$15 Control and authentication
$315.39 +$15 Control and authentication
$61.95 +$15 Control and authentication
$428.03 +$15 Control and authentication
$177.97 +$15 Control and authentication
$90.11$75.47 +$15 Control and authentication
$259.84$214.37 +$15 Control and authentication
$191.49$96.87 +$15 Control and authentication
$58.46$51.97 +$15 Control and authentication
$225.28 +$15 Control and authentication
$202.75 +$15 Control and authentication
$202.75 +$15 Control and authentication
$135.17 +$15 Control and authentication
$675.84$563.20 +$15 Control and authentication
$168.96$102.04 +$15 Control and authentication
$78.85 +$15 Control and authentication
$333.41 +$15 Control and authentication
$146.43 +$15 Control and authentication
$788.48$732.16 +$15 Control and authentication
$158.30 +$15 Control and authentication
$253.44$214.02 +$15 Control and authentication
$242.18 +$15 Control and authentication
$281.74 +$15 Control and authentication
$281.60 +$15 Control and authentication
$202.75$155.44 +$15 Control and authentication
$605.74$373.31 +$15 Control and authentication
$389.76 +$15 Control and authentication
$633.92$373.31 +$15 Control and authentication
$168.96$112.64 +$15 Control and authentication
$157.70 +$15 Control and authentication
$305.31$279.33 +$15 Control and authentication
$422.61$366.26 +$15 Control and authentication
$93.54 +$15 Control and authentication
$399.87 +$15 Control and authentication
$309.76 +$15 Control and authentication
$298.50$281.60 +$15 Control and authentication
$168.96$135.17 +$15 Control and authentication
$393.11 +$15 Control and authentication
$90.11$41.68 +$15 Control and authentication
$179.10 +$15 Control and authentication
$314.27$288.38 +$15 Control and authentication
$315.39$241.05 +$15 Control and authentication
$50.69$46.18 +$15 Control and authentication
$225.28 +$15 Control and authentication
$130$110 +$15 Control and authentication
$292.86$246.68 +$15 Control and authentication
$130$110 +$15 Control and authentication
$974.39 +$15 Control and authentication
$881.97 +$15 Control and authentication
$110.43 +$15 Control and authentication
$95.74 +$15 Control and authentication
$236.54$191.49 +$15 Control and authentication
$433.66$388.61 +$15 Control and authentication
$355.94 +$15 Control and authentication
$112.64$86.73 +$15 Control and authentication
$337.92$268.08 +$15 Control and authentication
$315.39$281.60 +$15 Control and authentication
$370.59 +$15 Control and authentication
$377.53 +$15 Control and authentication
$408.88 +$15 Control and authentication
$52 +$15 Control and authentication
$180.22 +$15 Control and authentication
$360.45 +$15 Control and authentication
$540.67$439.30 +$15 Control and authentication
$315.39$202.75 +$15 Control and authentication
$54.07$42.80 +$15 Control and authentication
$146.43 +$15 Control and authentication
$101.38$99.39 +$15 Control and authentication
$77.95 +$15 Control and authentication
$450.56$397.62 +$15 Control and authentication
$394.24$336.79 +$15 Control and authentication
$84.48 +$15 Control and authentication
$104.76$94.62 +$15 Control and authentication
$84.48 +$15 Control and authentication
$439.30 +$15 Control and authentication
$258.89$255.77 +$15 Control and authentication
$95.74$92.76 +$15 Control and authentication
$154.32 +$15 Control and authentication
$112.64$109.26 +$15 Control and authentication
$191.49 +$15 Control and authentication
$1,559.03$1,429.11 +$15 Control and authentication
$50.69 +$15 Control and authentication
$185.86 +$15 Control and authentication
$168.96$152.06 +$15 Control and authentication
$234.80 +$15 Control and authentication
$253.44$167.83 +$15 Control and authentication
$247.81$180.22 +$15 Control and authentication
$247.81 +$15 Control and authentication
$397.74 +$15 Control and authentication
$560.66 +$15 Control and authentication
$123.90$75.47 +$15 Control and authentication
$259.07$221.90 +$15 Control and authentication
$180 +$15 Control and authentication
$371.71$259.07 +$15 Control and authentication
$337.92$332.29 +$15 Control and authentication
$394.24 +$15 Control and authentication
$309.76$247.81 +$15 Control and authentication
$77.95$67.56 +$15 Control and authentication
Sold at $252.61 on November 22, 2022
$167.83 +$15 Control and authentication
$130$110 +$15 Control and authentication
$337.92 +$15 Control and authentication
$281.60 +$15 Control and authentication
$112.64$69.84 +$15 Control and authentication
$281.60 +$15 Control and authentication
$77.95$76.65 +$15 Control and authentication
$145.31 +$15 Control and authentication
$326.66$292.86 +$15 Control and authentication
$61.95$58.57 +$15 Control and authentication
$129.54 +$15 Control and authentication
$135.17$84.48 +$15 Control and authentication
$664.58$551.94 +$15 Control and authentication
$608.26 +$15 Control and authentication
$119.86$112.66 +$15 Control and authentication
$168.96$126.16 +$15 Control and authentication
$664.58$653.31 +$15 Control and authentication
$146.43$118.27 +$15 Control and authentication
$73.22$67.58 +$15 Control and authentication
$398 +$15 Control and authentication
$64.96$57.16 +$15 Control and authentication
$112.64$95.74 +$15 Control and authentication
Sold at $39.77 on November 22, 2022
$546.58$422.61 +$15 Control and authentication
$146.43 +$15 Control and authentication
$438.17$224.15 +$15 Control and authentication
$519.68$297.52 +$15 Control and authentication
$61.95 +$15 Control and authentication
$107.01 +$15 Control and authentication
$247.81$129.54 +$15 Control and authentication
$64.96$50.67 +$15 Control and authentication
$337.92 +$15 Control and authentication
$84.48 +$15 Control and authentication
$202.75 +$15 Control and authentication
$155.90$123.42 +$15 Control and authentication
$454.72 +$15 Control and authentication
$326.66$306.38 +$15 Control and authentication
$75.35 +$15 Control and authentication
$70.16 +$15 Control and authentication
$149.41 +$15 Control and authentication
$435.01$366.26 +$15 Control and authentication
$48.44 +$15 Control and authentication
$337.92$225.28 +$15 Control and authentication
$428.03 +$15 Control and authentication
$332.29 +$15 Control and authentication
$157.70 +$15 Control and authentication
$281.60$252.98 +$15 Control and authentication
$234.29 +$15 Control and authentication
$321.02$292.86 +$15 Control and authentication
$540.67$439.30 +$15 Control and authentication
$225.28 +$15 Control and authentication
Sold at $147.72 on November 21, 2022
$332.29$309.76 +$15 Control and authentication
$55.86$42.48 +$15 Control and authentication
$225.28$223.03 +$15 Control and authentication
$258.53 +$15 Control and authentication
$152.06 +$15 Control and authentication
$546.30 +$15 Control and authentication
$439.30 +$15 Control and authentication
$270.34 +$15 Control and authentication
$163.33 +$15 Control and authentication
$478.72$388.61 +$15 Control and authentication
$309.76$259.07 +$15 Control and authentication
$214.02$105.88 +$15 Control and authentication
$112.64$78.85 +$15 Control and authentication
$371.71 +$15 Control and authentication
$349.18 +$15 Control and authentication
$326.66$202.75 +$15 Control and authentication
$77.95$50.67 +$15 Control and authentication
$449.43$422.40 +$15 Control and authentication
$103.63 +$15 Control and authentication
$467.46$304.13 +$15 Control and authentication
$135.17 +$15 Control and authentication
$371.71 +$15 Control and authentication
$107.01$84.48 +$15 Control and authentication
$225.28 +$15 Control and authentication
$112.64 +$15 Control and authentication
$152.06$137.42 +$15 Control and authentication
$101.38$99.39 +$15 Control and authentication
$405.50$295.91 +$15 Control and authentication
$66.26$58.46 +$15 Control and authentication
$135.17$107.01 +$15 Control and authentication
$619.52 +$15 Control and authentication
$281.60 +$15 Control and authentication
$360.45 +$15 Control and authentication
$270.34$197.12 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$360.45$273.72 +$15 Control and authentication
$225.28 +$15 Control and authentication
$171.21$154.32 +$15 Control and authentication
$182.57 +$15 Control and authentication
$247.81$218.65 +$15 Control and authentication
$166.71 +$15 Control and authentication
$168.96 +$15 Control and authentication
$1,559.03 +$15 Control and authentication
$321.02$290.81 +$15 Control and authentication
$61.95 +$15 Control and authentication
$61.06$54.57 +$15 Control and authentication
$315.39 +$15 Control and authentication
$236.54 +$15 Control and authentication
$335.59$186.97 +$15 Control and authentication
$112.64$50.69 +$15 Control and authentication
$506.88$225.28 +$15 Control and authentication
$370.59 +$15 Control and authentication
$360.45$257.95 +$15 Control and authentication
$495.62 +$15 Control and authentication
$281.60$264.70 +$15 Control and authentication
$493.05$490.23 +$15 Control and authentication
$330.04 +$15 Control and authentication
$156.57 +$15 Control and authentication
$59.76$36.38 +$15 Control and authentication
$215.14 +$15 Control and authentication
$428.03$275.97 +$15 Control and authentication
$107.87$103.08 +$15 Control and authentication
$433.66$264.70 +$15 Control and authentication
$411.14$259.07 +$15 Control and authentication
$349.18$270.34 +$15 Control and authentication
$50.69 +$15 Control and authentication
$619.52 +$15 Control and authentication
$253.44 +$15 Control and authentication
$135.17 +$15 Control and authentication
$1,039.35 +$15 Control and authentication
$439.30$371.05 +$15 Control and authentication
$332.29 +$15 Control and authentication
$84.48$27.03 +$15 Control and authentication
$202.75$190.36 +$15 Control and authentication
$111.51 +$15 Control and authentication
$225.28$168.96 +$15 Control and authentication
$130$92 +$15 Control and authentication
$999 +$15 Control and authentication
$281.60 +$15 Control and authentication
$95.74$88.99 +$15 Control and authentication
$84.48$50.69 +$15 Control and authentication
$1,126.40$1,070.08 +$15 Control and authentication
$123.90$69.84 +$15 Control and authentication
$89$80 +$15 Control and authentication
$428.03 +$15 Control and authentication
$135.17$123.90 +$15 Control and authentication
$39.42 +$15 Control and authentication
$760.70$633.92 +$15 Control and authentication
$506.88$321.02 +$15 Control and authentication
$844.80 +$15 Control and authentication
$140.80$76.60 +$15 Control and authentication
$190.36$126.16 +$15 Control and authentication
$157.70$135.17 +$15 Control and authentication
$111.51$50.69 +$15 Control and authentication
$411.14 +$15 Control and authentication
$50.67$25.98 +$15 Control and authentication
$349.18$264.70 +$15 Control and authentication
$214.02$144.18 +$15 Control and authentication
$77.95$66.26 +$15 Control and authentication
$157.70$100.25 +$15 Control and authentication
$140.80 +$15 Control and authentication
$247 +$15 Control and authentication
$551.94 +$15 Control and authentication
$1,002.50$991.23 +$15 Control and authentication
$225.28$168.96 +$15 Control and authentication
$61.95$27.03 +$15 Control and authentication
$157.70$123.90 +$15 Control and authentication
$337.92$281.60 +$15 Control and authentication
$135.17 +$15 Control and authentication
$264.84 +$15 Control and authentication
$337.92$225.28 +$15 Control and authentication
$146.43$135.17 +$15 Control and authentication
$1,056.53 +$15 Control and authentication
$193.74$149.81 +$15 Control and authentication
$563.20 +$15 Control and authentication
$360.45 +$15 Control and authentication
$315.39 +$15 Control and authentication
$506.88$450.56 +$15 Control and authentication
$332.29 +$15 Control and authentication
$112.64 +$15 Control and authentication
$202.75 +$15 Control and authentication
$167.83$147.56 +$15 Control and authentication
$225.28$114.89 +$15 Control and authentication
$202.75$140.80 +$15 Control and authentication
$180.22 +$15 Control and authentication
$428.03$382.98 +$15 Control and authentication
$889.86$777.22 +$15 Control and authentication
$428.03$402.85 +$15 Control and authentication
$500.09$408.52 +$15 Control and authentication
$957.44 +$15 Control and authentication
$106.02 +$15 Control and authentication
$337.92 +$15 Control and authentication
$45.06$40.55 +$15 Control and authentication
$196.87$106.92 +$15 Control and authentication
$247.81$218.65 +$15 Control and authentication
$394.24$370.59 +$15 Control and authentication
$371.71 +$15 Control and authentication
$168.96$121.65 +$15 Control and authentication
$224.15$202.75 +$15 Control and authentication
$224.15$202.75 +$15 Control and authentication
$224.15$202.75 +$15 Control and authentication
$281.60$224.15 +$15 Control and authentication
$259.07$221.90 +$15 Control and authentication
$321.02 +$15 Control and authentication
$394.24$281.60 +$15 Control and authentication
$844.48 +$15 Control and authentication
$84.48$58.57 +$15 Control and authentication
$450.56$345.80 +$15 Control and authentication
$337.92$321.02 +$15 Control and authentication
$720.90$709.63 +$15 Control and authentication
$88.99 +$15 Control and authentication
$111.51 +$15 Control and authentication
$225.28$135.17 +$15 Control and authentication
$352.18 +$15 Control and authentication
$332.29$258.41 +$15 Control and authentication
$200.50 +$15 Control and authentication
$127.77$80.06 +$15 Control and authentication
$101.38$72.09 +$15 Control and authentication
$224.15 +$15 Control and authentication
$773.02 +$15 Control and authentication
$89.64$50.67 +$15 Control and authentication
$107.01 +$15 Control and authentication
$310 +$15 Control and authentication
$77.72$47.31 +$15 Control and authentication
$112.64$75.47 +$15 Control and authentication
$91.24 +$15 Control and authentication
$35
$536
$536
$125
$980
$235
$825
$66
$425$266
$390$178
$350
$410$349
$50
$50
$30
$325
$150
$450$365
$257$219
$395$350
$375$345
$449$320
$450$350
$370
$660
$515
$360$310
$693$683 +$15 Control and authentication
$374
$277
$284$255
$425$405
$475$360
$575
$260$250
$237
$224
$420
$160
$160
$375$359
$245
$32
$449$325
Sold at $386 on November 22, 2022
$285$250
$363
$1,595$1,435 +$15 Control and authentication
$375$350
$673 +$15 Control and authentication
$277
$390$365 +$15 Control and authentication
$399$299
$673 +$15 Control and authentication
$295
$125
$380
$196
$280
$65
$65
$59
$28
$160
$1,595$895 +$15 Control and authentication
$35
$125
$37
$58
$40
$112
$250
$141
$112
$250
$35
$168
$750$360
$390
$475
$319$270
$1,036$1,023 +$15 Control and authentication
$134
$141
$880 +$15 Control and authentication
$99
$399
$126$111
$395
$400$360
$1,575 +$15 Control and authentication
$824 +$15 Control and authentication
$350
$450$395
Sold at $75 on November 17, 2022
$250
$450$370
$111
$139
$200$179
$50
$255
$700
$895 +$15 Control and authentication
$162 +$15 Control and authentication
$149
$283
$299$287
$100
$350$225
$350
$360
$212
$600$300
$385$185
$982 +$15 Control and authentication
$775 +$15 Control and authentication
$299$268
$273
$25
$200
$789 +$15 Control and authentication
$100
$120
$119
$271
$125
$480 +$15 Control and authentication
$273
$486 +$15 Control and authentication
$243$183
$75
$170
$475
$995$806 +$15 Control and authentication
$984
$319$290
$518
$875
$815 +$15 Control and authentication
$410
$1,840 +$15 Control and authentication
$300
Sold at $47 on November 17, 2022
$984 +$15 Control and authentication
$238
$368.64 +$15 Control and authentication
$95
$195$149
$250
$410
$475
$1,671
$410
$410
$1,011 +$15 Control and authentication
$1,011 +$15 Control and authentication
$85
$54
$128
$68
$72
$232
$850 +$15 Control and authentication
$40
$1,387 +$15 Control and authentication
$216
$38$33
$149
$60
$61
$575 +$15 Control and authentication
$980$550
$96
$119
$250$134
$50$40
$300 +$15 Control and authentication
$57$49
$89
$76
$349
$89
$597
$45
$599$280
$95$51
$600
$22
$725
$180
$77
$452$407
$611
$1,200$1,079 +$15 Control and authentication
$380
$385$300
$385
$4,875$2,744.39 +$15 Control and authentication
$399
$73
$38
$43
$350
$4,400$3,159.35 +$15 Control and authentication
$32
$35
$339
$770$425 +$15 Control and authentication
$190
$480$429
$45$41
$230
$197
$285
$198$189
$324.80$257.24
$610$440
$198$189
$26
$515
$399$351
$68
$81
$325$301.16
$736
$625
$430
$63
$66
$499
$569
$90$27
$120
$350$316.64
$20
$125
$40
$266
$26
$165
$97
$132
$158
$45.06 +$15 Control and authentication
$45.06 +$15 Control and authentication
$103.94 +$15 Control and authentication
$45.06 +$15 Control and authentication
$112.64$73.22 +$15 Control and authentication
$323.28 +$15 Control and authentication
$225.28 +$15 Control and authentication
$245.55 +$15 Control and authentication
$371.71$337.92 +$15 Control and authentication
$337.92 +$15 Control and authentication
$170.09 +$15 Control and authentication
$101.38 +$15 Control and authentication
$110.39 +$15 Control and authentication
Sold at $78.85 on November 23, 2022
$275.97$248.93 +$15 Control and authentication
$135.17 +$15 Control and authentication
$833.54$720.90 +$15 Control and authentication
$540.67$370.59 +$15 Control and authentication
$229.79$203.88 +$15 Control and authentication
$202.75$168.96 +$15 Control and authentication
$506.88$475.34 +$15 Control and authentication
$111.51 +$15 Control and authentication
$337.92 +$15 Control and authentication
$337.92 +$15 Control and authentication
$191.49 +$15 Control and authentication
$714.56 +$15 Control and authentication
$563.20 +$15 Control and authentication
$302.57 +$15 Control and authentication
$50.69 +$15 Control and authentication
$664.58 +$15 Control and authentication
$202.75 +$15 Control and authentication
Sold at $215.90 on November 21, 2022
$219.65 +$15 Control and authentication
$929.28 +$15 Control and authentication
$78.85 +$15 Control and authentication
$929.28 +$15 Control and authentication
$394.24 +$15 Control and authentication
$422.24$401.45 +$15 Control and authentication
$247.81 +$15 Control and authentication
$532.79 +$15 Control and authentication
$208.38$200.50 +$15 Control and authentication
$140.31$126.02 +$15 Control and authentication
$584.64$454.72 +$15 Control and authentication
$163 +$15 Control and authentication
$1,125.27$968.70 +$15 Control and authentication
$111.51 +$15 Control and authentication
Sold at $103.25 on November 23, 2022
$497 +$15 Control and authentication
$224.15$174.59 +$15 Control and authentication
$157.70 +$15 Control and authentication
$107.01 +$15 Control and authentication
$223.03$202.75 +$15 Control and authentication
$232.56 +$15 Control and authentication
$301.88 +$15 Control and authentication
$240.35 +$15 Control and authentication
$68$62 +$15 Control and authentication
$255.94 +$15 Control and authentication
$518.14 +$15 Control and authentication
$101.38$92.36 +$15 Control and authentication
$394.24$270.34 +$15 Control and authentication
$168.96$153.19 +$15 Control and authentication
$225.28 +$15 Control and authentication
$449.43 +$15 Control and authentication
$78.85 +$15 Control and authentication
$325.53 +$15 Control and authentication
Sold at $183.37 on November 22, 2022
$704 +$15 Control and authentication
$1,039.35$519.68 +$15 Control and authentication
$326.66$247.81 +$15 Control and authentication
$146.43$123.90 +$15 Control and authentication
$574.46$506.88 +$15 Control and authentication
$298.50$236.54 +$15 Control and authentication
$394.24 +$15 Control and authentication
$506.88 +$15 Control and authentication
$224.15 +$15 Control and authentication
$506.88 +$15 Control and authentication
$168.96$152.06 +$15 Control and authentication
$337.92 +$15 Control and authentication
$236.54$202.75 +$15 Control and authentication
$202.75 +$15 Control and authentication
$1,036.29 +$15 Control and authentication
$162.40 +$15 Control and authentication
$394.24 +$15 Control and authentication
$198.25 +$15 Control and authentication
$281.60$180.22 +$15 Control and authentication
$197.12 +$15 Control and authentication
$540.67$370.59 +$15 Control and authentication
$493.05 +$15 Control and authentication
$202.75 +$15 Control and authentication
$270.34$212.89 +$15 Control and authentication
$263.58 +$15 Control and authentication
$67.58 +$15 Control and authentication
Sold at $168.96 on November 22, 2022
$191.49 +$15 Control and authentication
$506.88 +$15 Control and authentication
$189.24$170.09 +$15 Control and authentication
$382.98 +$15 Control and authentication
$76.60 +$15 Control and authentication
$160.75 +$15 Control and authentication
$562.07$449.43 +$15 Control and authentication
$285.82$253.34 +$15 Control and authentication
$160.75$149.27 +$15 Control and authentication
$192.28$187.08 +$15 Control and authentication
$1,239.04$1,182.72 +$15 Control and authentication
$180.22$126.16 +$15 Control and authentication
$202.75$188.11 +$15 Control and authentication
$76.65$71.46 +$15 Control and authentication
$167.83 +$15 Control and authentication
$332.29 +$15 Control and authentication
$247.81$230.91 +$15 Control and authentication
$315.39 +$15 Control and authentication
$449.43 +$15 Control and authentication
$162.40$129.92 +$15 Control and authentication
$449.43 +$15 Control and authentication
$169.04 +$15 Control and authentication
$947.17 +$15 Control and authentication
$281.60$140.80 +$15 Control and authentication
$337.92 +$15 Control and authentication
$271.46 +$15 Control and authentication
$202.75 +$15 Control and authentication
$259.07$247.81 +$15 Control and authentication
$92.36$84.48 +$15 Control and authentication
$118.66 +$15 Control and authentication
$292.86 +$15 Control and authentication
$202.75 +$15 Control and authentication
$247.81$202.75 +$15 Control and authentication
$168.96$163.33 +$15 Control and authentication
$112.64 +$15 Control and authentication
$224.15 +$15 Control and authentication
$431.33 +$15 Control and authentication
$107.01 +$15 Control and authentication
$168.96$157.70 +$15 Control and authentication
$168.96 +$15 Control and authentication
$161.08$152.06 +$15 Control and authentication
$337.92 +$15 Control and authentication
$272.83 +$15 Control and authentication
$506.88$394.24 +$15 Control and authentication
$281.60$247.81 +$15 Control and authentication
$225.28$209.51 +$15 Control and authentication
$103.94 +$15 Control and authentication
$270.34$241.05 +$15 Control and authentication
$428.03 +$15 Control and authentication
$337.92$304.13 +$15 Control and authentication
$111.51 +$15 Control and authentication
$505.75 +$15 Control and authentication
$349.18 +$15 Control and authentication
$619.52 +$15 Control and authentication
$332.29$325.53 +$15 Control and authentication
$505.75 +$15 Control and authentication
$219.65$137.42 +$15 Control and authentication
$242.18 +$15 Control and authentication
$511.39 +$15 Control and authentication
$360.45$325.53 +$15 Control and authentication
$97.44$87.05 +$15 Control and authentication
$140.80$118.27 +$15 Control and authentication
$704 +$15 Control and authentication
$698.37 +$15 Control and authentication
$337.92 +$15 Control and authentication
$1,103.87$957.44 +$15 Control and authentication
$73.22 +$15 Control and authentication
$191.49 +$15 Control and authentication
$87.86$56.32 +$15 Control and authentication
$426.91 +$15 Control and authentication
$135.17 +$15 Control and authentication
$224.15$168.96 +$15 Control and authentication
$135.17 +$15 Control and authentication
$394.24$354.82 +$15 Control and authentication
$657.16 +$15 Control and authentication
$506.88$450.56 +$15 Control and authentication
$428.03$337.92 +$15 Control and authentication
$378.74$372.75 +$15 Control and authentication
$281.60 +$15 Control and authentication
$337.92 +$15 Control and authentication
$259.07 +$15 Control and authentication
$156.57$146.43 +$15 Control and authentication
$337.92$202.75 +$15 Control and authentication
$157.20$80.55 +$15 Control and authentication
$202.75 +$15 Control and authentication
$61.95 +$15 Control and authentication
$562.07 +$15 Control and authentication
$394.24$343.55 +$15 Control and authentication
$135.17$107.01 +$15 Control and authentication
Sold at $42.12 on November 16, 2022
$112.64 +$15 Control and authentication
$123.90$111.51 +$15 Control and authentication
$224.15 +$15 Control and authentication
$326.66 +$15 Control and authentication
$146.43$135.17 +$15 Control and authentication
$134.04$84.48 +$15 Control and authentication
$467.46 +$15 Control and authentication
$467.46 +$15 Control and authentication
$64.96 +$15 Control and authentication
$122.78$112.64 +$15 Control and authentication
$315.39 +$15 Control and authentication
$90.11$73.22 +$15 Control and authentication
$259.07$199.37 +$15 Control and authentication
$281.60$137.42 +$15 Control and authentication
$261.23$134.93 +$15 Control and authentication
$562.07$398.75 +$15 Control and authentication
$238.80 +$15 Control and authentication
$337.92 +$15 Control and authentication
$415.74 +$15 Control and authentication
$257.95 +$15 Control and authentication
$100.25$86.73 +$15 Control and authentication
$337.92 +$15 Control and authentication
$844.80$674.71 +$15 Control and authentication
$214.02$202.75 +$15 Control and authentication
$230 +$15 Control and authentication
$360.45 +$15 Control and authentication
$332.29 +$15 Control and authentication
$107.01$84.48 +$15 Control and authentication
$360.45 +$15 Control and authentication
$428.03 +$15 Control and authentication
$168.96 +$15 Control and authentication
$225.28$185.86 +$15 Control and authentication
$519.68$435.23 +$15 Control and authentication
$135.17$87.86 +$15 Control and authentication
$150$100 +$15 Control and authentication
$168.96 +$15 Control and authentication
$168.96 +$15 Control and authentication
$253.44 +$15 Control and authentication
$381.85 +$15 Control and authentication
$73.22 +$15 Control and authentication
$168.96 +$15 Control and authentication
$95.74$72.09 +$15 Control and authentication
$77.72$49.56 +$15 Control and authentication
$135.17$61.95 +$15 Control and authentication
$202.75$123.90 +$15 Control and authentication
$563.48 +$15 Control and authentication
$168.96$137.42 +$15 Control and authentication
$506.88$450.56 +$15 Control and authentication
$337.92$332.29 +$15 Control and authentication
$957.44$844.80 +$15 Control and authentication
$200.50$189.24 +$15 Control and authentication
$394.24 +$15 Control and authentication
$225.28$202.75 +$15 Control and authentication
$84.48 +$15 Control and authentication
$349.18 +$15 Control and authentication
$366.08$224.15 +$15 Control and authentication
$332.29 +$15 Control and authentication
$394.24 +$15 Control and authentication
$433.66$415.64 +$15 Control and authentication
$1,182.72$878.59 +$15 Control and authentication
$67.58 +$15 Control and authentication
$202.75$61.95 +$15 Control and authentication
$604.33 +$15 Control and authentication
$259.07 +$15 Control and authentication
$168.96$140.80 +$15 Control and authentication
$157.70$107.01 +$15 Control and authentication
$112.64$73.22 +$15 Control and authentication
$491.11 +$15 Control and authentication
$189.24 +$15 Control and authentication
$281.60$252.31 +$15 Control and authentication
$494.49 +$15 Control and authentication
$79.97$50.69 +$15 Control and authentication
$150$107 +$15 Control and authentication
$557.57$512.51 +$15 Control and authentication
$263.68$191.77 +$15 Control and authentication
$506.88$450.56 +$15 Control and authentication
$111.51$60.83 +$15 Control and authentication
$337.92$325.53 +$15 Control and authentication
$281.60$180.22 +$15 Control and authentication
$95.74$86.73 +$15 Control and authentication
$135.17$109.26 +$15 Control and authentication
$270.34 +$15 Control and authentication
$50.69 +$15 Control and authentication
$95.74 +$15 Control and authentication
$281.60$259.07 +$15 Control and authentication
$111.51$65.33 +$15 Control and authentication
$264.70$208.38 +$15 Control and authentication
$259.07 +$15 Control and authentication
$199.37$185.86 +$15 Control and authentication
$100$91 +$15 Control and authentication
$127.28$114.89 +$15 Control and authentication
$281.60 +$15 Control and authentication
$190.36$125.03 +$15 Control and authentication
$546.30 +$15 Control and authentication
$78.85$61.95 +$15 Control and authentication
$315.39 +$15 Control and authentication
$78.85$64.20 +$15 Control and authentication
$562.07$501.25 +$15 Control and authentication
$506.88$473.09 +$15 Control and authentication
$64.20$56.32 +$15 Control and authentication
$337.92 +$15 Control and authentication
$194.88$87.05 +$15 Control and authentication
$247.81 +$15 Control and authentication
$40.55 +$15 Control and authentication
$225.28$188.11 +$15 Control and authentication
$394.24$309.76 +$15 Control and authentication
$1,092.61$884.22 +$15 Control and authentication
$253.44$157.70 +$15 Control and authentication
$112.64$67.58 +$15 Control and authentication
$281.60$253.44 +$15 Control and authentication
$450.56 +$15 Control and authentication
$123.90 +$15 Control and authentication
$270.34$253.44 +$15 Control and authentication
$92.36$56.32 +$15 Control and authentication
$236.54 +$15 Control and authentication
$152.06$101.38 +$15 Control and authentication
$551.94 +$15 Control and authentication
$324$281.74 +$15 Control and authentication
$394.24$168.96 +$15 Control and authentication
$585.73$506.88 +$15 Control and authentication
$90.11 +$15 Control and authentication
$1,464.32 +$15 Control and authentication
$259.07 +$15 Control and authentication
$674.71 +$15 Control and authentication'''


a = a.split('\n')

file = open('op.txt','a')
import re
for ind,val  in enumerate(a)  :
    a[ind] = (re.sub("[a-zA-Z+ ]","",val))
    # print(a[ind])
    file.write(a[ind]+'\n')
file.close()