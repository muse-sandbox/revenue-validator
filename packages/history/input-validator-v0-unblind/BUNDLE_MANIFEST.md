# FLOW-565 evaluation input bundle

Prepared on 2026-08-04 after completion of the valid FLOW-546 clean blind-run.

The bundle contains three immutable input groups:

- eight verbatim blind-run outputs plus the run manifest and clean-room declaration;
- the holdout ground truth and mapping;
- the pre-registered evaluation protocol.

The eight blind-output hashes below match the output hashes recorded during FLOW-546.

## SHA-256

```text
9d70f0696366722f0950b1d7b6744b13fc1cea8a5010b28a07934ee2d5267359  blind-run/blind_outputs/HX-01.md
544225df05f1e58bd40b7eade25205252b44465af257d91ab503fee987815eb2  blind-run/blind_outputs/HX-02.md
8997acc282a5e57d318958fc447d73003cea3502928e42a5da066e260c4f7d60  blind-run/blind_outputs/HX-03.md
a79f8f611ab0fad4e7affb12fdb19c97d18d418b8ea28730a7948fae686953ba  blind-run/blind_outputs/HX-04.md
9bbbc0de41ee9f3bd492f2e687137897e7ba4d13b6e423ca416e2e62fe56cec3  blind-run/blind_outputs/HX-05.md
79be7ed68921f920569621804b299862d2cc43eaf4e764857099c318cb6a132c  blind-run/blind_outputs/HX-06.md
87ba6e85b195e9262099bec62adb6b573f29b5f4541233fe42d9bd2ee62619b3  blind-run/blind_outputs/HX-07.md
95f79c505228236c7608aa9f3e3df19676ad6693ce16bd0a03e711ae5af02e37  blind-run/blind_outputs/HX-08.md
34d532cd159e5bc804f0540c2aead771ce50cf92a16ad3d2c90ad794a8ec17f1  blind-run/run_manifest.md
2ac25c88c24162b0835c7e4cad2eaf9ed26c698e5c1b4931803cf972164a23f9  blind-run/clean_room_declaration.md
8eddfd8ad18cb5a07baf7ba29bacd6951a32bd105a97c1d2c571ed92c93846ba  blind-run/blind_run_summary.md
20e7b042069b46412c62b6772230d8465abdecbfa64cafdae6ecc171d8257c04  ground-truth/HX-01_gt.md
4230accc9f38b99e7c45fa6de4fdb738027c244736d84c5ffa4c191e23fee33a  ground-truth/HX-02_gt.md
4bf4f597fc62cbe4f058daa6307ee02137fed84dfc316db2399976d485a2e093  ground-truth/HX-03_gt.md
e2b012574d94906c22d11bbf922f8973c9d99098410951eaed78a778d83e0738  ground-truth/HX-04_gt.md
70ad0a32df4091c8e5d8b00238f849f58479913e30ebe483b0a98129dc700d0d  ground-truth/HX-05_gt.md
f5432b95a268c1046032e59f5839436217b775002356133c7fb691b0245252de  ground-truth/HX-06_gt.md
4607a16ed1421c5bafa8b6f16af3bb32cd2a79dedf371a04c95cff7387fb18d9  ground-truth/HX-07_gt.md
e846e4382de114bcb65189de61ed70cfa5683f5b4e06b2c5af6121a5e937a613  ground-truth/HX-08_gt.md
ad3f10c96c334a45a1b2f0412011cbf15ceef77e0ba22d7301c5df4403d25315  ground-truth/ground_truth_master.md
7abe3719dc857252793e6200d10584edd4373b3d472badcb4ffa9c437a2ff5ad  ground-truth/mapping.md
87c5b2578588e32b944a04d67ce0302f1901ee7fea850d83ae5135c63e46601c  ground-truth/warehouse_facts.md
e71906a34a63a4526dd1212730911a76ac5289cd59f27999f8d8f6481bdec31c  EVALUATION_PROTOCOL.md
```

Do not rerun Validator V0 or edit the blind outputs. This bundle is for evaluation only.
