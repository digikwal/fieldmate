# Changelog

## [1.13.0](https://github.com/digikwal/fieldmate/compare/v1.12.0...v1.13.0) (2025-08-11)


### Features

* Add x_href field for settings custom html to uploaded files ([33b931f](https://github.com/digikwal/fieldmate/commit/33b931f8b27ff03778d46d0b4b834e40562d5b9f))

## [1.12.0](https://github.com/digikwal/fieldmate/compare/v1.11.1...v1.12.0) (2025-08-11)


### Features

* add before/after app install hooks to validate dependencies and setup fields ([a4b09e1](https://github.com/digikwal/fieldmate/commit/a4b09e133321871046dd785c741b07f9d01072a9))
* add centralized custom field setup with per-doctype control ([f2ff049](https://github.com/digikwal/fieldmate/commit/f2ff04986d9309127bf9c182bed32bd646e8185e))
* add install hooks and doc_events for safe custom field lifecycle management ([d8c37ee](https://github.com/digikwal/fieldmate/commit/d8c37eede0a3f496441bac4fe537f9dde6c045f5))
* Add new templates and components for enhanced UI and functionality ([af264d7](https://github.com/digikwal/fieldmate/commit/af264d721e4dfb0e5b901041780ab4e2f5cb8564))
* add tag and release ([ff453fd](https://github.com/digikwal/fieldmate/commit/ff453fd0d8f2f6585278d094609e1a41d6e50075))
* ci auto merge logic ([2942fd1](https://github.com/digikwal/fieldmate/commit/2942fd1a88dbf4048e7508351ddfaf31da27cd39))
* **ci:** add auto merge ([e95452c](https://github.com/digikwal/fieldmate/commit/e95452c5afefef1433fc3f17fb464c36d8bd2855))
* **ci:** add workflow dispatch ([e913642](https://github.com/digikwal/fieldmate/commit/e91364226a2fa317549e552e2f590d972a81186a))
* **ci:** add workflow dispatch ([c2010ae](https://github.com/digikwal/fieldmate/commit/c2010aecb7be118cfecadaf4ee0454f1aafef4de))
* **ci:** get dynamic pr number ([b4c1b3a](https://github.com/digikwal/fieldmate/commit/b4c1b3a6f8281d70f45530f51c442bee34d37ce0))
* correct fine grained token permissions ([8fbb27b](https://github.com/digikwal/fieldmate/commit/8fbb27b028a20c33fd4ae6dc1679604e27d8aa17))
* create auto-pr ([7d4f84b](https://github.com/digikwal/fieldmate/commit/7d4f84b3ccc16830a490d05ba1bdc5decc33370a))
* cross repo auto pr ([d0a393d](https://github.com/digikwal/fieldmate/commit/d0a393d416e3a339103815dca72234f0fda51ad5))
* cross repo pat permissions ([787f921](https://github.com/digikwal/fieldmate/commit/787f9217033683cbff5249022b73f2aac8d0bcb3))
* export all x_fieldmate fields to versioned JSON with change detection ([f49a664](https://github.com/digikwal/fieldmate/commit/f49a664997ee159c0422c7ed5a55b604f80f8223))
* export script now removes obsolete field JSON files to stay in sync with DB ([4c39f3a](https://github.com/digikwal/fieldmate/commit/4c39f3a548df4cdce693b92386e810b580e73338))
* initial release for versioning ([3515ed7](https://github.com/digikwal/fieldmate/commit/3515ed78456f26ef559e7397c0b2a53c42a4fd40))
* initial release for versioning ([3fdc1ee](https://github.com/digikwal/fieldmate/commit/3fdc1ee0d6dc5d61e8730749ca0700f40d3f5778))
* initial release for versioning ([4917202](https://github.com/digikwal/fieldmate/commit/4917202fd1d9c0c1c22259c87b5119682784fd8b))
* initial release for versioning ([7b6c79d](https://github.com/digikwal/fieldmate/commit/7b6c79d14a3d80f2ff502a76454f6325fe27b2c5))
* initial release for versioning ([b918c1d](https://github.com/digikwal/fieldmate/commit/b918c1dcb468dea89cb99564715edfd3badf59b0))
* Initialize App ([fc1ecd2](https://github.com/digikwal/fieldmate/commit/fc1ecd262257cbd5c1690cdb664e12508a87191a))
* Remove custom 404 page fixture from hooks.py ([6da55b6](https://github.com/digikwal/fieldmate/commit/6da55b61f5812e486878153358c347e0702da006))
* Remove deprecated 404 route fixture and update web template structure ([70c58c9](https://github.com/digikwal/fieldmate/commit/70c58c9d9012130a5ae721d0ee9449a47ce673b9))
* repository dispatch build trigger ([aca4236](https://github.com/digikwal/fieldmate/commit/aca423642670160eef6ca86a847e0b6dc4acb00f))
* Update include paths to remove redundant 'fieldmate' prefix in templates ([8c7718a](https://github.com/digikwal/fieldmate/commit/8c7718aea10204970683ff20aa64f1ec45f076d5))


### Bug Fixes

* add checkout step ([29243d3](https://github.com/digikwal/fieldmate/commit/29243d30866bb8665d0ab55406fbedcbcf1af553))
* add gh_pat ([6e70ace](https://github.com/digikwal/fieldmate/commit/6e70acebdf9d489869fdeeb595dcc174235f0a74))
* add gh_token ([3c109d8](https://github.com/digikwal/fieldmate/commit/3c109d830b35972e40efc646abdfa04ecdada855))
* add permissions ([70f970a](https://github.com/digikwal/fieldmate/commit/70f970a3541aa9770b0c71c7b341c801763dac94))
* add workflow triggers ([781d40a](https://github.com/digikwal/fieldmate/commit/781d40a3044155384231a8d0c2bc5ee30f37cf76))
* checkout path ([68708c7](https://github.com/digikwal/fieldmate/commit/68708c7672c38b58d75db39918abcd2dbe2a64f4))
* ci trigger on target ([d2ab49b](https://github.com/digikwal/fieldmate/commit/d2ab49bd35597ff2118e61afe1de2d13047b3891))
* **ci:** create release step filter ([19d48dd](https://github.com/digikwal/fieldmate/commit/19d48dd4d3b3d3676ed2bcbee321aa21b24a73d2))
* **ci:** define config file ([026bc67](https://github.com/digikwal/fieldmate/commit/026bc67fa0bbffcadff47340d53bdaec8cad00d3))
* **ci:** force ignore manifest ([6c8ea13](https://github.com/digikwal/fieldmate/commit/6c8ea132bd04da2ea71d1c848c4c06d1323693be))
* **ci:** gh pr merge syntax ([edac3d8](https://github.com/digikwal/fieldmate/commit/edac3d8ea29355f47bee955ddc05c00f16c142fe))
* **ci:** set manifest file ([54255a9](https://github.com/digikwal/fieldmate/commit/54255a941978fed029500d0437533a63003e8cfe))
* **ci:** set path ([59d5ba6](https://github.com/digikwal/fieldmate/commit/59d5ba6213dd69ebf48f26c138ae52d3d16b11de))
* Correct project description in pyproject.toml ([9123630](https://github.com/digikwal/fieldmate/commit/91236301e592e553f2ef12b39e41fdecdd717f36))
* Custom Fields cannot be added to core DocTypes ([854870e](https://github.com/digikwal/fieldmate/commit/854870e1f390c802608b9bca3d445ef034ea17a1))
* define config location ([1709037](https://github.com/digikwal/fieldmate/commit/1709037568d507c78601edb0e150330fc606afd8))
* error in yaml syntax on line 38 ([ae9178e](https://github.com/digikwal/fieldmate/commit/ae9178e1deb689135dd7d206ef97b7d6123bdca6))
* error in yaml syntax on line 38 ([b7dbe06](https://github.com/digikwal/fieldmate/commit/b7dbe06ac001acb60e9f220e00bfd2645f445f9a))
* move release-please config to root ([71dbf5a](https://github.com/digikwal/fieldmate/commit/71dbf5a24c7b0c153af9290da80e3910943c3e1c))
* path to app install function ([10c5499](https://github.com/digikwal/fieldmate/commit/10c5499218f75bfce315bc0f162ceeeac5efe423))
* **refactor:** optimize hook with single-field logic and guard ([cb1321f](https://github.com/digikwal/fieldmate/commit/cb1321fb2fa20441b79d4038cf27085b2ad3abe0))
* remove [bot] from github actor filter ([303de6b](https://github.com/digikwal/fieldmate/commit/303de6bc3483adb2f4cf4204751fa64b4876410c))
* remove fixtures logic ([0290cc3](https://github.com/digikwal/fieldmate/commit/0290cc3165daa243ed4a2e745830ef324da4ea00))
* rename to release-please-config.json ([111f63f](https://github.com/digikwal/fieldmate/commit/111f63f8fc3c8a61f3b6b5e4fb7b1515046abcc0))
* restructure directories and files ([4f10023](https://github.com/digikwal/fieldmate/commit/4f10023cfbbd9de3fc519a20ad51040ee86d2eb6))
* Update include paths to use the correct template directory structure ([902dff0](https://github.com/digikwal/fieldmate/commit/902dff032abfb3fd87f2f708aac37d1671fd9c2d))

## [1.11.1](https://github.com/digikwal/fieldmate/compare/v1.11.0...v1.11.1) (2025-07-30)


### Bug Fixes

* Update include paths to use the correct template directory structure ([902dff0](https://github.com/digikwal/fieldmate/commit/902dff032abfb3fd87f2f708aac37d1671fd9c2d))

## [1.11.0](https://github.com/digikwal/fieldmate/compare/v1.10.0...v1.11.0) (2025-07-30)


### Features

* Update include paths to remove redundant 'fieldmate' prefix in templates ([8c7718a](https://github.com/digikwal/fieldmate/commit/8c7718aea10204970683ff20aa64f1ec45f076d5))

## [1.10.0](https://github.com/digikwal/fieldmate/compare/v1.9.0...v1.10.0) (2025-07-30)


### Features

* Remove custom 404 page fixture from hooks.py ([6da55b6](https://github.com/digikwal/fieldmate/commit/6da55b61f5812e486878153358c347e0702da006))

## [1.9.0](https://github.com/digikwal/fieldmate/compare/v1.8.0...v1.9.0) (2025-07-30)


### Features

* Remove deprecated 404 route fixture and update web template structure ([70c58c9](https://github.com/digikwal/fieldmate/commit/70c58c9d9012130a5ae721d0ee9449a47ce673b9))

## [1.8.0](https://github.com/digikwal/fieldmate/compare/v1.7.1...v1.8.0) (2025-07-30)


### Features

* Add new templates and components for enhanced UI and functionality ([af264d7](https://github.com/digikwal/fieldmate/commit/af264d721e4dfb0e5b901041780ab4e2f5cb8564))

## [1.7.1](https://github.com/digikwal/fieldmate/compare/v1.7.0...v1.7.1) (2025-06-29)


### Bug Fixes

* **refactor:** optimize hook with single-field logic and guard ([cb1321f](https://github.com/digikwal/fieldmate/commit/cb1321fb2fa20441b79d4038cf27085b2ad3abe0))

## [1.7.0](https://github.com/digikwal/fieldmate/compare/v1.6.2...v1.7.0) (2025-06-27)


### Features

* **ci:** add workflow dispatch ([e913642](https://github.com/digikwal/fieldmate/commit/e91364226a2fa317549e552e2f590d972a81186a))


### Bug Fixes

* error in yaml syntax on line 38 ([ae9178e](https://github.com/digikwal/fieldmate/commit/ae9178e1deb689135dd7d206ef97b7d6123bdca6))
* error in yaml syntax on line 38 ([b7dbe06](https://github.com/digikwal/fieldmate/commit/b7dbe06ac001acb60e9f220e00bfd2645f445f9a))

## [1.6.2](https://github.com/digikwal/fieldmate/compare/v1.6.1...v1.6.2) (2025-06-27)


### Bug Fixes

* Custom Fields cannot be added to core DocTypes ([854870e](https://github.com/digikwal/fieldmate/commit/854870e1f390c802608b9bca3d445ef034ea17a1))

## [1.6.1](https://github.com/digikwal/fieldmate/compare/v1.6.0...v1.6.1) (2025-06-26)


### Bug Fixes

* path to app install function ([10c5499](https://github.com/digikwal/fieldmate/commit/10c5499218f75bfce315bc0f162ceeeac5efe423))

## [1.6.0](https://github.com/digikwal/fieldmate/compare/v1.5.1...v1.6.0) (2025-06-26)


### Features

* cross repo pat permissions ([787f921](https://github.com/digikwal/fieldmate/commit/787f9217033683cbff5249022b73f2aac8d0bcb3))

## [1.5.1](https://github.com/digikwal/fieldmate/compare/v1.5.0...v1.5.1) (2025-06-26)


### Bug Fixes

* checkout path ([68708c7](https://github.com/digikwal/fieldmate/commit/68708c7672c38b58d75db39918abcd2dbe2a64f4))

## [1.5.0](https://github.com/digikwal/fieldmate/compare/v1.4.1...v1.5.0) (2025-06-26)


### Features

* cross repo auto pr ([d0a393d](https://github.com/digikwal/fieldmate/commit/d0a393d416e3a339103815dca72234f0fda51ad5))

## [1.4.1](https://github.com/digikwal/fieldmate/compare/v1.4.0...v1.4.1) (2025-06-26)


### Bug Fixes

* restructure directories and files ([4f10023](https://github.com/digikwal/fieldmate/commit/4f10023cfbbd9de3fc519a20ad51040ee86d2eb6))

## [1.4.0](https://github.com/digikwal/fieldmate/compare/v1.3.0...v1.4.0) (2025-06-26)


### Features

* correct fine grained token permissions ([8fbb27b](https://github.com/digikwal/fieldmate/commit/8fbb27b028a20c33fd4ae6dc1679604e27d8aa17))

## [1.3.0](https://github.com/digikwal/fieldmate/compare/v1.2.0...v1.3.0) (2025-06-26)


### Features

* repository dispatch build trigger ([aca4236](https://github.com/digikwal/fieldmate/commit/aca423642670160eef6ca86a847e0b6dc4acb00f))

## [1.2.0](https://github.com/digikwal/fieldmate/compare/v1.1.0...v1.2.0) (2025-06-25)


### Features

* add tag and release ([ff453fd](https://github.com/digikwal/fieldmate/commit/ff453fd0d8f2f6585278d094609e1a41d6e50075))
* initial release for versioning ([3515ed7](https://github.com/digikwal/fieldmate/commit/3515ed78456f26ef559e7397c0b2a53c42a4fd40))
* initial release for versioning ([3fdc1ee](https://github.com/digikwal/fieldmate/commit/3fdc1ee0d6dc5d61e8730749ca0700f40d3f5778))
* initial release for versioning ([4917202](https://github.com/digikwal/fieldmate/commit/4917202fd1d9c0c1c22259c87b5119682784fd8b))


### Bug Fixes

* add gh_pat ([6e70ace](https://github.com/digikwal/fieldmate/commit/6e70acebdf9d489869fdeeb595dcc174235f0a74))
* add permissions ([70f970a](https://github.com/digikwal/fieldmate/commit/70f970a3541aa9770b0c71c7b341c801763dac94))
