import numpy as np
from nipype.testing import assert_true
import tempfile
from nipype.algorithms.misc import calc_moments


def test_skew():
    data = """14.62418305  5.916396751  -1.658088086  4.71113546  1.598428608  5.612553811  -5.004056368  -4.057513911
11.16365251  17.32688599  -3.099920667  2.630189741  2.389709914  0.379332731  -0.2899694205  -4.363591482
2.059205599  23.90705054  0.7180462297  -1.976963652  7.487682025  -5.583986129  1.094800525  -2.319858134
-1.907579712  22.08277347  4.595575886  -3.869054671  8.214834769  -3.442156385  2.428766374  0.7736184662
0.6535290043  14.1320384  0.9458768261  -2.577892846  -0.8925440241  3.177128674  6.048546332  1.736059675
3.149271524  8.106285467  -6.173280371  -0.5146958863  -11.83574747  4.066575201  9.160589786  0.1680632718
3.089673173  8.736851925  -5.624227736  1.386441126  -12.58621755  -0.726443824  8.036414499  -0.3318169666
2.685349599  9.968755255  2.965603277  2.634928414  -3.783441929  -1.858587372  3.238274675  2.594880211
0.870577208  2.323455904  7.840351954  1.635436162  2.451630603  2.834494164  -1.384081764  5.840475644
-4.421008251  -12.78755879  2.985581265  -1.609381512  -0.1816579797  5.448215202  -2.855889998  5.041186537
-8.502455278  -22.66799593  -3.964218147  -4.180363107  -5.061764789  2.439737668  -0.9988071581  1.437142327
-5.355058719  -19.00567875  -4.803737548  -3.884369973  -4.977945181  -0.4758749938  1.894453988  0.003263759218
1.29682909  -8.295173365  -1.51226274  -1.611159469  -2.5403281  -0.2155584519  2.597114132  1.16528519
3.162947556  -3.093405654  0.4782790153  1.015061011  -2.755821487  -1.015685899  0.1402527399  0.05435017236
0.9158883917  -6.679241736  0.9376568982  3.175011335  -2.712383777  -3.836563374  -2.270503748  -4.593165145
0.5468675209  -11.14130502  1.420140475  3.506045445  2.777240829  -3.14187819  -0.7823285883  -6.84663074
-0.5754863055  -9.638785593  0.2926825231  1.039079149  9.613209645  1.300380032  3.755092776  -2.30881605
-9.12095608  -5.422145216  -3.089096046  -1.913969236  8.36828235  1.622740946  6.756285589  4.803793558
-18.6459149  -5.677906762  -4.447399529  -1.826561667  -1.179681537  -3.51737806  6.062770694  7.743917051
-14.12032005  -9.346953111  -0.3927872312  0.5116398162  -8.814603334  -4.191932775  3.735940996  5.926107194
3.984986352  -7.490234063  5.101302343  0.6359344324  -8.098435707  3.372259941  1.603560776  2.787631701
16.74369044  2.523688856  4.825375014  -2.888386026  -2.929939078  7.41176576  -0.9444665519  -0.5476924783
13.0864062  10.44887074  -2.409155335  -6.466987193  2.038766622  -0.9844478726  -3.872608358  -3.903240663
3.888161509  7.356308659  -9.783752602  -6.593576679  7.785360016  -11.59798121  -5.359996968  -4.646576281
2.919034842  0.4926039084  -9.765686304  -3.169484175  13.3885185  -10.00053277  -5.284251069  -1.953467094
7.762685816  3.138596183  -2.417670781  2.087535944  12.09072814  0.3201456619  -5.986630196  -0.393473785
8.598656701  12.64638617  4.32929224  6.665685612  2.52013659  4.924021467  -7.729146671  -2.531538284
4.286211902  12.70121508  4.197284784  7.586579174  -4.511459665  1.039992021  -7.200406996  -2.678018972
-0.206805413  -1.118395095  1.251956053  4.927663964  -0.3269306726  -1.614001868  -2.858296125  3.708027659
-3.615745533  -13.26040515  4.163662563  3.376525012  6.876574727  1.021356663  1.813515644  9.401028448
-6.392625018  -11.19412506  11.70010341  5.557449086  3.188483207  3.033109557  3.108015432  5.00732323
-5.697688304  -1.564055358  12.53451981  6.641295722  -9.330508253  1.60952695  1.985401431  -4.635334005
-0.4739120366  5.308731294  3.209488234  1.907340382  -15.26443399  1.262158357  1.288838724  -6.54661201
3.733208755  11.99608217  -4.121352088  -3.787629919  -8.977806581  3.760241115  1.048439633  -0.2497259139
1.633682769  21.98252106  0.008457593931  -2.863301753  -1.475378656  4.854200462  -0.156717616  2.028483989
-4.262983941  24.73198623  6.529712692  1.286325062  -1.857794734  2.962236297  -1.586154566  -3.6478191
-7.502330557  10.60931417  2.397686502  -1.56459968  -4.721655517  2.006857078  -1.490344215  -7.044842318
-5.198726771  -8.273929595  -7.6127574  -11.03862432  -1.592101433  3.747829535  -0.06779667515  -2.412618507
0.7334095101  -11.76661769  -9.165804187  -14.81298889  5.36362746  4.955331255  1.673488979  2.0899358
5.517823916  -1.529874203  -2.421802273  -6.947139589  8.366593034  3.55375893  4.03335273  -0.05524186477
1.474077483  2.649817521  7.255506458  6.068405441  -2.220943179  -0.6343270953  1.382522916  -2.748044018
-6.776840898  2.855345278  -3.570626044  1.654853143  -2.838161622  0.755210647  7.252510904  1.235575241
-14.86022341  -0.8943548346  -10.36165869  -1.966680076  -3.641426564  -3.670112785  8.644955043  6.859610046
-7.145239483  -0.1458937017  -3.867994525  -0.9484554762  -2.48227248  -8.36071796  2.539637492  5.399990929
8.804929045  1.925551314  3.240568033  1.273961559  2.104351411  -6.141864838  -5.255423549  -0.7896387751
9.735755254  -1.862844212  -2.552156104  -0.3902178948  5.745817797  -1.515932976  -8.546922674  -3.440929455
-5.837957148  -8.226266393  -13.20837554  -4.385043051  2.553090991  -4.209818986  -8.331176217  -1.707250641
-12.64051676  -8.2399894  -12.76990779  -5.960467624  -4.294427772  -10.92374675  -8.6902905  0.3421994093
1.17028221  -1.953361346  -2.607159313  -4.896369845  -4.519583123  -8.055510792  -9.019182555  3.36412153
14.48433641  2.152584104  3.178007658  -3.9792054  3.873546228  5.321306118  -5.445499499  8.684509027
8.116988393  0.4683619278  1.046001596  -3.128586059  10.0250152  12.58326776  1.447856102  10.18164703
-4.706381289  -1.788728553  0.6563335204  -0.5831451131  5.744824049  3.988876139  5.65836796  2.189197844
-2.76704126  -0.495980308  6.533235978  2.372759856  -2.792331174  -7.896310272  3.502571539  -8.556072249
8.315654337  0.7043190657  11.38508989  2.565286445  -5.081739754  -6.900720718  -1.667312154  -10.59024727
9.909297104  -2.934946689  8.968652164  -0.5610029798  -0.6957945725  3.815352939  -4.277309457  -4.346939024
3.809478921  -8.178727502  2.78966603  -4.568498377  3.295953611  9.457549108  -2.931773943  -0.04922082646
4.940986376  -6.906199411  -0.6726182267  -6.550149966  3.251783239  6.324220141  0.1496185048  -1.7701633
10.55846735  1.720423345  -0.02248084003  -4.475053837  0.3943175795  3.615274407  3.17786214  -4.661015894
5.164991215  7.975239079  2.030845129  1.259865261  -3.543706118  6.424886561  5.257164014  -5.686755714
-7.85360929  4.585684687  2.641661508  6.399259194  -5.791994946  9.620021677  5.059618162  -5.841773643
-7.887333445  -1.663863126  0.531225876  6.442066641  -2.580841985  8.356612294  2.609875283  -3.391732494
7.467417207  0.7346301535  -2.719728468  2.822035284  4.54698989  4.221046784  0.791568596  3.728706407
14.76100347  9.382305581  -3.17219641  1.381585183  7.754995237  -0.3908054543  1.355349478  9.807914939
0.1267792801  9.818588278  0.5608772817  3.633460684  3.711951896  -5.421004876  1.162611597  7.001274262
-19.35283277  -2.103358718  4.16130701  4.67192889  -0.8231375514  -8.81474386  -2.846417531  -1.268859264
-20.80038431  -11.76135621  2.944594891  1.64388247  -0.1668629943  -6.707442921  -6.544901517  -3.830974298
-5.592905106  -6.057725588  -1.233208621  -1.339964983  0.7299911265  -0.7530015377  -3.117175727  1.142381884
7.890421323  8.119524766  -2.606602104  0.007101965698  -4.473969864  1.35750371  5.357618774  4.161238035
9.600782899  14.52365435  0.1990637024  3.403466406  -11.59507852  -3.675154543  8.718678202  0.7825822225
3.703846665  8.748127367  3.135332804  4.127582534  -12.38852274  -9.447080613  3.417599727  -1.915488323
-3.011725724  -0.5381126202  3.567929983  2.184591464  -7.411651508  -9.252946446  -1.827784625  1.560496584
-7.142629796  -5.355184696  3.289780212  1.113331632  -3.105505654  -5.606446238  0.1961208934  6.334603712
-6.659543803  -4.245675975  3.726757782  1.953178495  -0.7484610023  -4.426403774  3.716311729  6.200735049
-1.643440395  0.7536090906  2.509268017  2.15471156  2.374200456  -3.774138064  -0.1428981969  2.646676328
3.686406766  4.827058909  -2.458101484  -0.39559615  5.082577298  3.167157352  -8.147321924  -0.03506891856
4.407495284  2.5606793  -8.149493446  -4.632729429  4.938050013  14.56344531  -9.374945991  -1.3893417
-0.1687177084  -4.106757231  -9.343602374  -7.415904922  4.749022091  18.81314153  -1.749200795  -2.02566815
-6.507688641  -6.001538055  -6.108916568  -6.784929595  7.21051134  10.59847744  5.776257506  -0.4990570991
-9.820082348  -0.5741078285  -4.687969138  -4.377866052  7.40862329  -0.06470407472  6.857336593  2.745243336
-7.04365894  2.689020958  -8.804350547  -3.506610093  0.5732906688  -1.771827007  4.332768659  3.537426733
-0.4346222942  -2.295147419  -12.91289393  -3.95705062  -7.130741497  1.478867856  2.340197798  -0.2224791818
2.355519667  -7.446912611  -8.580935982  -1.515500603  -6.545362285  -2.460234117  0.4822626914  -5.261252431
-3.230857748  -4.456435972  3.105258325  4.868182005  -0.3155725672  -12.9461276  -1.81314629  -7.915543953
-10.61694158  1.023409988  11.23695246  9.13393953  2.080132446  -15.68433051  -2.452603277  -8.067702457
-8.952785439  0.3914623321  9.072213866  5.788054925  0.5661677477  -4.862572943  -1.253393229  -6.497656047
1.825216246  -2.868761361  2.684946057  -1.702605515  2.524615008  6.658427102  -1.464383881  -3.333412097
10.52499456  -1.807928838  1.602770946  -5.693835167  7.025193015  6.172728664  -3.989160551  -0.7754719889
10.83430082  0.3010957187  5.703164372  -4.7215044  5.747620411  -0.6137370397  -5.393253651  -1.967790019
9.084992271  -1.297359974  7.313272774  -2.919262371  -0.341939585  -0.488964096  -3.962652217  -5.129527247
11.86896398  -0.4901633845  3.193953846  -1.811431925  -0.3604987261  6.192234507  -2.348495577  -4.159036411
14.81736012  7.870835671  -2.04922723  0.122245812  7.807201578  8.435263453  -1.994392703  2.494961459
10.99679669  13.62141018  -3.175917696  1.68947873  12.43613872  4.131979444  -0.8035598171  8.583091116
3.538171963  6.008200439  0.5876902994  0.4403643142  6.183013749  2.012581919  1.090536757  8.392496526
0.5460594103  -6.259032909  6.647104433  -1.43557129  -3.452884137  4.366160275  -0.2274303705  3.900139848
1.772017802  -8.109091085  10.50095909  -0.1621391129  -7.608906136  2.481208401  -4.509906047  0.7763248812
0.606115406  -2.603199426  7.692974034  2.104967053  -8.226098406  -6.837921596  -4.561655055  1.015397953
-2.978847372  -2.385761908  -0.8339871055  0.6707971346  -9.874595181  -13.39338209  3.157380259  2.413897035
-2.985013991  -5.160444086  -7.29279473  -2.371762765  -10.03622895  -9.34912711  10.97609581  2.654665151
-1.068091568  -0.2479914452  -6.107351633  -0.9239821871  -5.835733231  -2.189236707  9.811317248  1.508754364
-6.520427038  7.430392097  -1.95095948  4.15525371  -2.032963385  -2.693509918  2.091753969  0.4782648423
-18.09299987  4.740223292  -2.838854108  6.118069011  -3.664423954  -7.91518773  -2.533067915  1.120941519
-19.32711056  -3.231687054  -8.04776777  3.689162869  -6.952885159  -6.854774161  -1.172264884  2.581894309
-2.203996345  -0.5339747203  -10.27858531  1.833505163  -5.406679162  1.678416611  0.871971912  1.837113402
15.60657966  8.749980935  -7.560269196  1.70515063  0.1003191195  8.04135078  1.044572756  -1.582641946
12.19564564  5.273436246  -4.367517279  -0.0400759142  4.431313549  7.067826794  2.741622337  -3.458851463
-6.44120462  -9.849684434  -1.946651925  -2.183436603  6.686267514  4.016449169  6.302612811  -0.9698019507
-13.80878408  -13.92578887  3.071419193  -0.156449455  8.551444945  4.051266929  5.541317929  1.901010931
-1.084801367  -1.267516734  9.774222689  3.461150291  8.195043157  4.77412064  -2.223359889  0.07143463336
11.95939854  7.195316999  11.93418631  1.472618288  3.247038347  2.656123844  -9.091445458  -4.097157466
-2.752420619  -1.103781682  -3.382675846  -3.9326499  0.3168555978  -2.600573426  -9.409987851  -1.564842317
-11.68718367  -12.62978052  -7.436711849  -11.05071165  -4.535693861  -4.973062537  -9.154275121  -0.8478464554
-11.1129098  -8.014294516  -5.818564146  -6.557508409  -4.920322355  -2.444494132  -0.762850219  -1.035995467
-0.1942650118  5.507757423  -0.6713848498  2.045539379  0.2907563314  2.654730384  5.268838031  -2.711154892
6.638825325  9.118078409  2.220738816  5.875202986  0.6059672284  -5.305207318  -0.08004872831  -2.950039659
12.18704972  0.6256114468  2.352153233  8.701077613  4.804756766  -6.163162012  -1.779998967  -6.493561445
4.442326811  -15.10908307  4.919949591  3.969210961  7.004029439  0.1398435001  -4.659976897  -3.899267451
-7.594265524  -20.77328745  5.94521557  -2.385814065  3.224509406  8.943882025  -3.270587613  3.470325906
-8.696673766  -12.29052026  -0.3763403003  -5.55470641  -3.51572569  12.51259902  3.753517263  8.67338497
-0.5057854071  -2.415896554  -9.663571931  -5.714041661  -6.037933426  8.673756933  10.03557773  8.629816199
3.622185659  0.4716627142  -10.92515308  -3.705286841  -2.776089545  2.271920902  9.251504922  5.744980887
"""
    with tempfile.NamedTemporaryFile(delete=True) as f:
        f.write(data)
        f.flush()
        skewness = calc_moments(f.name, 3)
        yield assert_true, np.allclose(skewness, np.array(
            [-0.23418937314622, 0.2946365564954823, -0.05781002053540932,
             -0.3512508282578762, -
             0.07035664150233077, -
             0.01935867699166935,
             0.00483863369427428, 0.21879460029850167]))
