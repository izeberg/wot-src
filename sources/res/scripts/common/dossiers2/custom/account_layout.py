from dossiers2.common.DossierBlockBuilders import *
from dossiers2.custom.dependencies import ACHIEVEMENT15X15_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENT7X7_DEPENDENCIES
from dossiers2.custom.dependencies import ACHIEVEMENTRATED7X7_DEPENDENCIES
from dossiers2.custom.dependencies import HISTORICAL_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import FALLOUT_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import FORT_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import SINGLE_ACHIEVEMENTS_DEPENDENCIES
from dossiers2.custom.dependencies import GLOBAL_MAP_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import RANKED_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import A30X30_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import EPIC_BATTLE_STATS_DEPENDENCIES
from dossiers2.custom.dependencies import STEAM_ACHIEVEMENT_DEPENDENCIES
from battle_statistics_layouts import *
TOTAL_BLOCK_LAYOUT = [
 'creationTime', 'lastBattleTime', 'battleLifeTime', 'treesCut', 'mileage']
_totalBlockBuilder = StaticSizeBlockBuilder('total', TOTAL_BLOCK_LAYOUT, {}, [])
_a15x15BlockBuilder = StaticSizeBlockBuilder('a15x15', A15X15_BLOCK_LAYOUT, A15X15_STATS_DEPENDENCIES, [])
_a15x15_2BlockBuilder = StaticSizeBlockBuilder('a15x15_2', A15X15_2_BLOCK_LAYOUT, {}, [])
_clanBlockBuilder = StaticSizeBlockBuilder('clan', CLAN_BLOCK_LAYOUT, CLAN_STATS_DEPENDENCIES, [])
_clan2BlockBuilder = StaticSizeBlockBuilder('clan2', CLAN2_BLOCK_LAYOUT, {}, [])
_companyBlockBuilder = StaticSizeBlockBuilder('company', COMPANY_BLOCK_LAYOUT, {}, [])
_company2BlockBuilder = StaticSizeBlockBuilder('company2', COMPANY2_BLOCK_LAYOUT, {}, [])
_a7x7BlockBuilder = StaticSizeBlockBuilder('a7x7', A7X7_BLOCK_LAYOUT, A7X7_STATS_DEPENDENCIES, [])
_rated7x7BlockBuilder = StaticSizeBlockBuilder('rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_historicalBlockBuilder = StaticSizeBlockBuilder('historical', HISTORICAL_BLOCK_LAYOUT, HISTORICAL_STATS_DEPENDENCIES, [])
_fortBattlesInClanBlockBuilder = StaticSizeBlockBuilder('fortBattlesInClan', FORT_BLOCK_LAYOUT, {}, [])
_fortSortiesInClanBlockBuilder = StaticSizeBlockBuilder('fortSortiesInClan', FORT_BLOCK_LAYOUT, {}, [])
_fortBattlesBlockBuilder = StaticSizeBlockBuilder('fortBattles', FORT_BLOCK_LAYOUT, FORT_BATTLES_STATS_DEPENDENCIES, [])
_fortSortiesBlockBuilder = StaticSizeBlockBuilder('fortSorties', FORT_BLOCK_LAYOUT, FORT_SORTIES_STATS_DEPENDENCIES, [])
_globalMapMiddleBlockBuilder = StaticSizeBlockBuilder('globalMapMiddle', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_globalMapChampionBlockBuilder = StaticSizeBlockBuilder('globalMapChampion', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_globalMapAbsoluteBlockBuilder = StaticSizeBlockBuilder('globalMapAbsolute', GLOBAL_MAP_BLOCK_LAYOUT, GLOBAL_MAP_STATS_DEPENDENCIES, [])
_falloutBlockBuilder = StaticSizeBlockBuilder('fallout', FALLOUT_BLOCK_LAYOUT, FALLOUT_STATS_DEPENDENCIES, [])
_rankedBlockBuilder = StaticSizeBlockBuilder('ranked', RANKED_BLOCK_LAYOUT, RANKED_STATS_DEPENDENCIES, [])
_a30x30BlockBuilder = StaticSizeBlockBuilder('a30x30', A30X30_BLOCK_LAYOUT, A30X30_STATS_DEPENDENCIES, [])
_epicBattleBlockBuilder = StaticSizeBlockBuilder('epicBattle', EPIC_BATTLE_BLOCK_LAYOUT, EPIC_BATTLE_STATS_DEPENDENCIES, [])
_rankedSeason1BlockBuilder = StaticSizeBlockBuilder('rankedSeason1', RANKED_BLOCK_LAYOUT, {}, [])
_rankedSeason2BlockBuilder = StaticSizeBlockBuilder('rankedSeason2', RANKED_BLOCK_LAYOUT, {}, [])
_rankedSeason3BlockBuilder = StaticSizeBlockBuilder('rankedSeason3', RANKED_BLOCK_LAYOUT, {}, [])
_rankedArchiveBlockBuilder = StaticSizeBlockBuilder('rankedArchive', RANKED_BLOCK_LAYOUT, {}, [])
_ranked_10x10BlockBuilder = StaticSizeBlockBuilder('ranked_10x10', RANKED_BLOCK_LAYOUT, RANKED_STATS_DEPENDENCIES, [])
_max15x15BlockBuilder = StaticSizeBlockBuilder('max15x15', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_max7x7BlockBuilder = StaticSizeBlockBuilder('max7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder('maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxHistoricalBlockBuilder = StaticSizeBlockBuilder('maxHistorical', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortBattlesBlockBuilder = StaticSizeBlockBuilder('maxFortBattles', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortSortiesBlockBuilder = StaticSizeBlockBuilder('maxFortSorties', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortBattlesInClanBlockBuilder = StaticSizeBlockBuilder('maxFortBattlesInClan', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFortSortiesInClanBlockBuilder = StaticSizeBlockBuilder('maxFortSortiesInClan', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapMiddleBlockBuilder = StaticSizeBlockBuilder('maxGlobalMapMiddle', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapChampionBlockBuilder = StaticSizeBlockBuilder('maxGlobalMapChampion', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxGlobalMapAbsoluteBlockBuilder = StaticSizeBlockBuilder('maxGlobalMapAbsolute', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxFalloutBlockBuilder = StaticSizeBlockBuilder('maxFallout', MAX_FALLOUT_BLOCK_LAYOUT_WITH_AVATAR, {}, [])
_maxRankedBlockBuilder = StaticSizeBlockBuilder('maxRanked', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_max30x30BlockBuilder = StaticSizeBlockBuilder('max30x30', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxEpicBattleBlockBuilder = StaticSizeBlockBuilder('maxEpicBattle', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedSeason1BlockBuilder = StaticSizeBlockBuilder('maxRankedSeason1', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedSeason2BlockBuilder = StaticSizeBlockBuilder('maxRankedSeason2', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedSeason3BlockBuilder = StaticSizeBlockBuilder('maxRankedSeason3', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRankedArchiveBlockBuilder = StaticSizeBlockBuilder('maxRankedArchive', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
_maxRanked_10x10BlockBuilder = StaticSizeBlockBuilder('maxRanked_10x10', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])

class VEHICLE_STATS:
    FRAGS = 'vehTypeFrags'
    A15x15_CUT = 'a15x15Cut'
    A30x30_CUT = 'a30x30Cut'
    A7x7_CUT = 'a7x7Cut'
    HISTORICAL_CUT = 'historicalCut'
    FORT_SORTIES_CUT = 'fortSortiesCut'
    FORT_BATTLES_CUT = 'fortBattlesCut'
    RANKED_CUT = 'rankedCut'
    RANKED_CUT_SEASON_1 = 'rankedCutSeason1'
    RANKED_CUT_SEASON_2 = 'rankedCutSeason2'
    RANKED_CUT_SEASON_3 = 'rankedCutSeason3'
    RANKED_CUT_ARCHIVE = 'rankedCutArchive'
    RANKED_CUT_10X10 = 'rankedCut_10x10'
    RATED_7x7_CUT = 'rated7x7Cut'
    GLOBAL_MAP_COMMON_CUT = 'globalMapCommonCut'
    FALLOUT_CUT = 'falloutCut'
    MARK_OF_MASTERY_CUT = 'markOfMasteryCut'
    EPIC_BATTLE_CUT = 'epicBattleCut'
    ALL = (
     FRAGS, A15x15_CUT, A30x30_CUT, A7x7_CUT, HISTORICAL_CUT, FORT_SORTIES_CUT, FORT_BATTLES_CUT, RANKED_CUT,
     RANKED_CUT_SEASON_1, RANKED_CUT_SEASON_2, RANKED_CUT_SEASON_3, RANKED_CUT_ARCHIVE, RANKED_CUT_10X10,
     RATED_7x7_CUT, GLOBAL_MAP_COMMON_CUT, FALLOUT_CUT, MARK_OF_MASTERY_CUT, EPIC_BATTLE_CUT)


_vehTypeFragsBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FRAGS, 'I', 'H', VEH_TYPE_FRAGS_DEPENDENCIES)
_a15x15CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.A15x15_CUT, 'I', 'III', {})
_a7x7CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.A7x7_CUT, 'I', 'IIIIIII', {})
_rated7x7CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.RATED_7x7_CUT, 'I', 'IIIIIII', {})
_historicalCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.HISTORICAL_CUT, 'I', 'III', {})
_fortBattlesCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FORT_BATTLES_CUT, 'I', 'III', {})
_fortSortiesCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FORT_SORTIES_CUT, 'I', 'III', {})
_globalMapCommonCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.GLOBAL_MAP_COMMON_CUT, 'I', 'III', {})
_falloutCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.FALLOUT_CUT, 'I', 'IIII', {})
_rankedCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT, 'I', 'III', {})
_rankedCutSeason1BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_SEASON_1, 'I', 'III', {})
_rankedCutSeason2BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_SEASON_2, 'I', 'III', {})
_rankedCutSeason3BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_SEASON_3, 'I', 'III', {})
_rankedCutArchiveBlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_ARCHIVE, 'I', 'III', {})
_rankedCut10x10BlockBuilder = DictBlockBuilder(VEHICLE_STATS.RANKED_CUT_10X10, 'I', 'III', {})
_a30x30CutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.A30x30_CUT, 'I', 'III', {})
_markOfMasteryCut = DictBlockBuilder(VEHICLE_STATS.MARK_OF_MASTERY_CUT, 'I', 'B', {})
_epicBattleCutBlockBuilder = DictBlockBuilder(VEHICLE_STATS.EPIC_BATTLE_CUT, 'I', 'III', {})
_ACHIEVEMENTS15X15_BLOCK_LAYOUT = [
 'fragsBeast', 'sniperSeries', 'maxSniperSeries', 'invincibleSeries',
 'maxInvincibleSeries', 'diehardSeries', 'maxDiehardSeries', 'killingSeries',
 'fragsSinai',
 'maxKillingSeries', 'piercingSeries', 'maxPiercingSeries', 'battleHeroes',
 'warrior', 'invader',
 'sniper', 'defender', 'steelwall', 'supporter', 'scout', 'evileye', 'medalKay',
 'medalCarius',
 'medalKnispel', 'medalPoppel', 'medalAbrams', 'medalLeClerc', 'medalLavrinenko',
 'medalEkins',
 'medalWittmann', 'medalOrlik', 'medalOskin', 'medalHalonen', 'medalBurda',
 'medalBillotte',
 'medalKolobanov', 'medalFadin', 'medalRadleyWalters', 'medalBrunoPietro',
 'medalTarczay',
 'medalPascucci', 'medalDumitru', 'medalLehvaslaiho', 'medalNikolas',
 'medalLafayettePool',
 'sinai', 'heroesOfRassenay', 'beasthunter', 'mousebane', 'tankExpertStrg',
 'raider', 'kamikaze', 'lumberjack',
 'medalBrothersInArms', 'medalCrucialContribution', 'medalDeLanglade',
 'medalTamadaYoshio',
 'bombardier', 'huntsman', 'alaric', 'sturdy', 'ironMan', 'luckyDevil',
 'pattonValley',
 'fragsPatton', 'mechanicEngineerStrg', 'sniper2', 'mainGun',
 'medalMonolith', 'medalAntiSpgFire', 'medalGore', 'medalCoolBlood', 'medalStark',
 'maxWFC2014WinSeries', 'WFC2014WinSeries',
 'impenetrable', 'reliableComradeSeries', 'reliableComrade', 'maxAimerSeries',
 'shootToKill', 'fighter', 'duelist', 'demolition', 'arsonist', 'bonecrusher',
 'charmed', 'even',
 'maxDeathTrackWinSeries', 'deathTrackWinSeries', 'readyForBattleLT',
 'readyForBattleMT', 'readyForBattleHT', 'readyForBattleSPG', 'readyForBattleATSPG',
 'readyForBattleALL', 'tankwomenProgress', 'testartilleryman',
 'maxEFC2016WinSeries', 'EFC2016WinSeries', 'EFC2016Goleador',
 'markIBomberman', 'markIRepairer', 'markI100Years', 'rankedBattlesHeroProgress',
 'FE18ClosedStage', 'FE18SoloStriker', 'FE18SoloMidfielder', 'FE18SoloDefender',
 'readyForBattleAllianceUSSR', 'readyForBattleAllianceGermany',
 'readyForBattleAllianceUSA', 'readyForBattleAllianceFrance', 'superTesterVeteran',
 'RP2018firstmed', 'RP2018secondmed', 'RP2018thirdmed', 'RP2018sergeant',
 'BR2019Top1Solo', 'BR2019Top1Squad', 'superTesterVeteranCross',
 'rankedDivisionCounter', 'rankedDivisionFighter', 'rankedStayingCounter',
 'rankedStayingPower', 'collectorVehicleStrg', 'TenYearsCountdownStageMedal',
 'wtHunterWins', 'wtBossWins', 'wtSpecBossDefeat', 'RP2018sergeantCounter',
 'wtxHunterWins', 'wtxBossWins', 'wtxSpecBossDefeat',
 'whiteTiger2012', 'lunarNY2022Progression',
 'oowTankmanWins', 'oowStrategistWins', 'oowCompetetiveWin',
 'mapboxUniversal', 'wclTournamentParticipant', 'wclParticipant']
_achievements15x15PopUps = [
 'warrior', 'invader', 'sniper', 'defender', 'steelwall', 'supporter',
 'scout', 'medalKay', 'medalCarius', 'medalKnispel', 'medalPoppel', 'medalAbrams',
 'medalLeClerc',
 'medalLavrinenko', 'medalEkins', 'medalWittmann', 'medalOrlik', 'medalOskin',
 'medalHalonen',
 'medalBurda', 'medalBillotte', 'medalKolobanov', 'medalFadin', 'beasthunter', 'mousebane',
 'tankExpert', 'raider',
 'kamikaze', 'lumberjack', 'evileye', 'medalRadleyWalters', 'medalLafayettePool',
 'medalBrunoPietro', 'medalTarczay', 'medalPascucci', 'medalDumitru', 'medalLehvaslaiho',
 'medalNikolas', 'sinai', 'pattonValley', 'heroesOfRassenay', 'mechanicEngineer',
 'tankExpert0',
 'tankExpert1', 'tankExpert2', 'tankExpert3', 'tankExpert4', 'tankExpert5', 'tankExpert6',
 'tankExpert7', 'tankExpert8', 'tankExpert9', 'tankExpert10', 'tankExpert11',
 'tankExpert12',
 'tankExpert13', 'tankExpert14', 'mechanicEngineer0', 'mechanicEngineer1',
 'mechanicEngineer2',
 'mechanicEngineer3', 'mechanicEngineer4', 'mechanicEngineer5', 'mechanicEngineer6',
 'mechanicEngineer7', 'mechanicEngineer8', 'mechanicEngineer9', 'mechanicEngineer10',
 'mechanicEngineer11', 'mechanicEngineer12', 'mechanicEngineer13', 'mechanicEngineer14',
 'medalBrothersInArms', 'medalCrucialContribution', 'medalDeLanglade', 'medalTamadaYoshio',
 'bombardier', 'huntsman', 'alaric', 'sturdy', 'ironMan', 'luckyDevil', 'sniper2',
 'mainGun',
 'medalMonolith', 'medalAntiSpgFire', 'medalGore', 'medalCoolBlood',
 'medalStark',
 'impenetrable', 'reliableComrade',
 'shootToKill', 'fighter', 'duelist', 'demolition', 'arsonist', 'bonecrusher', 'charmed',
 'even',
 'readyForBattleLT', 'readyForBattleMT', 'readyForBattleHT', 'readyForBattleSPG',
 'readyForBattleATSPG', 'readyForBattleALL', 'testartilleryman', 'EFC2016Goleador',
 'markIBomberman', 'markIRepairer', 'markI100Years',
 'FE18ClosedStage', 'FE18SoloStriker', 'FE18SoloMidfielder', 'FE18SoloDefender',
 'readyForBattleAllianceUSSR', 'readyForBattleAllianceGermany',
 'readyForBattleAllianceUSA', 'readyForBattleAllianceFrance', 'superTesterVeteran',
 'RP2018firstmed', 'RP2018secondmed', 'RP2018thirdmed', 'RP2018sergeant', 'BR2019Top1Solo',
 'BR2019Top1Squad', 'superTesterVeteranCross', 'collectorVehicle', 'collectorVehicle0',
 'collectorVehicle1', 'collectorVehicle2', 'collectorVehicle3', 'collectorVehicle4',
 'collectorVehicle5', 'collectorVehicle6', 'collectorVehicle7',
 'collectorVehicle8', 'collectorVehicle9', 'collectorVehicle10', 'collectorVehicle11',
 'collectorVehicle12', 'collectorVehicle13', 'collectorVehicle14',
 'TenYearsCountdownStageMedal', 'wtHunterWins', 'wtBossWins', 'wtSpecBossDefeat',
 'wtxHunterWins', 'wtxBossWins', 'wtxSpecBossDefeat', 'lunarNY2022Progression',
 'oowTankmanWins', 'oowStrategistWins', 'oowCompetetiveWin', 'mapboxUniversal',
 'wclTournamentParticipant', 'wclParticipant']
_achievements15x15BlockBuilder = StaticSizeBlockBuilder('achievements', _ACHIEVEMENTS15X15_BLOCK_LAYOUT, ACHIEVEMENT15X15_DEPENDENCIES, _achievements15x15PopUps)
_STEAM_BLOCK_LAYOUT = [
 'steamBattleCredits', 'steamLittleSavingsMedal', 'steamMintedCoinMedal', 'steamKingMidasMedal',
 'steamBattleXP', 'steamGoodStudentMedal', 'steamBattleHardenedMedal', 'steamExperienceMedal',
 'steamFreeXP', 'steamHandyMedal', 'steamUniversalResourceMedal', 'steamPowerKnowledgeMedal',
 'steamSuchWorkMedal', 'steamNothingPersonalMedal', 'steamTheBeginningMedal',
 'steamMasteryMarks',
 'steamGetMaxMedal', 'steamThreeCheersMedal', 'steamGoldenFiveMedal',
 'steamNotPerfectMedal', 'steamForWarriorMedal', 'steamForSteelWallMedal',
 'steamForBonecrusherMedal', 'steamOrderMedal', 'steamSpottedMedal', 'steamFighterMedal',
 'steamBasePoints', 'steamBasePointsMedal', 'steamHardCharacter', 'steamHardCharacterMedal',
 'steamMedium', 'steamMediumMedal', 'steamATSPG', 'steamATSPGMedal', 'steamDieHardMedal',
 'steamDestroyerMedal', 'steamMediumPerformanceMedal', 'steamReconnoiter',
 'steamReconnoiterMedal',
 'steamPotentialStun', 'steamPotentialStunMedal', 'steamMileage', 'steamMileageMedal',
 'steamHorizonSupportMedal', 'steamSmallSupportMedal', 'steamBreakThrough',
 'steamBreakThroughMedal', 'steamStop', 'steamStopMedal', 'steamRandomFightMedal',
 'steamMainGunMedal', 'steamBootcampMedal', 'steamBriefingMedal',
 'steamDoPotapovQuestMedal', 'steamDoAllBranchPotapovQuestMedal', 'steamDoOperationMedal',
 'steamGetTankLevel5Medal', 'steamGetTankLevel6Medal', 'steamGetTankLevel7Medal',
 'steamGetTankLevel8Medal', 'steamGetTankLevel9Medal', 'steamGetTankLevel10Medal',
 'steamShellTypeMedal', 'steamEquipTypeMedal', 'steamLastHeroMedal', 'steamShootToKillMedal',
 'steamBruteForceMedal', 'steamGuerrillaMedal', 'steamImpenetrableMedal', 'steamTurnOffMedal',
 'steamRadioMedal', 'steamTopLeague', 'steamTopLeagueMedal', 'steamSpotted', 'steamFrags',
 'steamBattleHeroes']
_steamAchievementsPopUps = []
_steamAchievementsLogRecords = ['steamLittleSavingsMedal', 'steamMintedCoinMedal', 'steamKingMidasMedal',
 'steamGoodStudentMedal', 'steamBattleHardenedMedal', 'steamExperienceMedal',
 'steamHandyMedal', 'steamUniversalResourceMedal', 'steamPowerKnowledgeMedal',
 'steamSuchWorkMedal', 'steamNothingPersonalMedal', 'steamTheBeginningMedal',
 'steamGetMaxMedal', 'steamThreeCheersMedal', 'steamGoldenFiveMedal',
 'steamNotPerfectMedal', 'steamForWarriorMedal', 'steamForSteelWallMedal',
 'steamForBonecrusherMedal', 'steamOrderMedal', 'steamSpottedMedal',
 'steamFighterMedal', 'steamBasePointsMedal', 'steamHardCharacterMedal',
 'steamMediumMedal', 'steamATSPGMedal', 'steamDieHardMedal', 'steamDestroyerMedal',
 'steamMediumPerformanceMedal', 'steamReconnoiterMedal', 'steamPotentialStunMedal',
 'steamMileageMedal', 'steamHorizonSupportMedal', 'steamSmallSupportMedal',
 'steamBreakThroughMedal', 'steamStopMedal', 'steamRandomFightMedal',
 'steamMainGunMedal', 'steamGetTankLevel5Medal', 'steamGetTankLevel6Medal',
 'steamGetTankLevel7Medal', 'steamGetTankLevel8Medal', 'steamGetTankLevel9Medal',
 'steamGetTankLevel10Medal', 'steamShellTypeMedal', 'steamEquipTypeMedal',
 'steamLastHeroMedal', 'steamShootToKillMedal', 'steamBruteForceMedal',
 'steamGuerrillaMedal', 'steamImpenetrableMedal', 'steamTurnOffMedal',
 'steamRadioMedal', 'steamTopLeagueMedal']
_steamAchievementsBlockBuilder = StaticSizeBlockBuilder('steamAchievements', _STEAM_BLOCK_LAYOUT, STEAM_ACHIEVEMENT_DEPENDENCIES, _steamAchievementsPopUps, _steamAchievementsLogRecords)
ACHIEVEMENTS7X7_BLOCK_LAYOUT = [
 'wolfAmongSheep', 'wolfAmongSheepMedal', 'geniusForWar',
 'geniusForWarMedal', 'kingOfTheHill', 'tacticalBreakthroughSeries',
 'maxTacticalBreakthroughSeries',
 'armoredFist', 'godOfWar', 'fightingReconnaissance', 'fightingReconnaissanceMedal',
 'willToWinSpirit', 'crucialShot', 'crucialShotMedal', 'forTacticalOperations',
 'promisingFighter', 'promisingFighterMedal', 'heavyFire', 'heavyFireMedal',
 'ranger', 'rangerMedal', 'fireAndSteel', 'fireAndSteelMedal', 'pyromaniac',
 'pyromaniacMedal', 'noMansLand',
 'guerrilla', 'guerrillaMedal', 'infiltrator', 'infiltratorMedal', 'sentinel',
 'sentinelMedal',
 'prematureDetonation', 'prematureDetonationMedal', 'bruteForce', 'bruteForceMedal',
 'awardCount', 'battleTested']
_achievement7x7PopUps = ['wolfAmongSheepMedal', 'geniusForWarMedal', 'kingOfTheHill', 'armoredFist',
 'godOfWar', 'forTacticalOperations', 'crucialShotMedal',
 'willToWinSpirit', 'fightingReconnaissanceMedal', 'promisingFighterMedal', 'heavyFireMedal',
 'rangerMedal', 'fireAndSteelMedal', 'pyromaniacMedal', 'noMansLand',
 'guerrillaMedal', 'infiltratorMedal', 'sentinelMedal', 'prematureDetonationMedal',
 'bruteForceMedal', 'battleTested']
_achievements7x7BlockBuilder = StaticSizeBlockBuilder('achievements7x7', ACHIEVEMENTS7X7_BLOCK_LAYOUT, ACHIEVEMENT7X7_DEPENDENCIES, _achievement7x7PopUps)
ACHIEVEMENTSRATED7X7_BLOCK_LAYOUT = [
 'tacticalAdvantage', 'tacticalSkill', 'secretOperations',
 'victoryMarchClubDBID', 'victoryMarchSeries', 'maxVictoryMarchSeries']
_achievementRated7x7PopUps = ['tacticalAdvantage', 'tacticalSkill', 'secretOperations']
_achievementsRated7x7BlockBuilder = StaticSizeBlockBuilder('achievementsRated7x7', ACHIEVEMENTSRATED7X7_BLOCK_LAYOUT, ACHIEVEMENTRATED7X7_DEPENDENCIES, _achievementRated7x7PopUps)
HISTORICAL_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'guardsman', 'makerOfHistory', 'bothSidesWins',
 'weakVehiclesWins']
_historicalAchievementsPopUps = ['guardsman', 'makerOfHistory']
_historicalAchievementsBlockBuilder = StaticSizeBlockBuilder('historicalAchievements', HISTORICAL_ACHIEVEMENTS_BLOCK_LAYOUT, HISTORICAL_ACHIEVEMENTS_DEPENDENCIES, _historicalAchievementsPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = [
 'titleSniper', 'invincible', 'diehard', 'handOfDeath',
 'armorPiercer', 'battleCitizen', 'WFC2014', 'tacticalBreakthrough', 'aimer',
 'deathTrack', 'firstMerit', 'tankwomen', 'operationWinter', 'victoryMarch', 'fallout',
 'fallout2', 'falloutSingleWolf', 'falloutPackOfWolfs', 'falloutSteelHunter',
 'falloutAlwaysInLine', 'moonSphere', 'EFC2016', 'markIProtector', 'markIBaseProtector',
 'xmasTreeBronze', 'xmasTreeSilver', 'xmasTreeGold',
 'rankedBattlesPioneer', 'HE17A1', 'HE17A2', 'HE17A3', 'NY18A1', 'NY18A2', 'NY18A3',
 'rankedBattlesHero', 'rankedBattlesSeasonOne',
 'FE18Universal', 'FE18Collection1', 'FE18Collection2', 'FE18Collection3',
 'FE18OpenRegistration', 'FE18OpenPlayOff', 'FE18OpenFinalStage', 'FE18OpenFirstPlace',
 'medalKursk', 'newMeritPM2', 'streamersEventUsha', 'streamersEventJove',
 'streamersEventAmway921', 'streamersEventLeBwA', 'twitchPrime',
 'alphaTester', 'betaTester', '10YearsOfService', '09YearsOfService', '08YearsOfService',
 '07YearsOfService', '06YearsOfService', '05YearsOfService', '04YearsOfService',
 '03YearsOfService', '02YearsOfService', '01YearsOfService', 'NY19A1',
 'NY19A2', 'NY19A3', 'epicBattle1', 'epicBattle2', 'epicBattle3', 'epicBattle4',
 'DdaymarathonMedal', 'twitchPrime2', 'twitchPrime3', 'se12019Medal',
 'Fest19Collection1', 'Fest19Collection2', 'Fest19Collection3', 'twitchPrime4',
 'BR2019Title25', 'BR2019Title15', 'BR2019Title5', 'october19', 'Fest19Offspring',
 'Fest19Racer', 'november19', 'december19', 'NY20A1', 'NY20A2', 'NY20A3', 'january20',
 'february20', 'medalBobLebwa', 'medalBobYusha', 'medalBobAmway921',
 'medalBobKorbenDallas', 'medalBobMailand', 'medalBobSkill4ltu', 'medalBobDezgamez',
 'medalBobAwesomeEpicGuys', 'medalBobTigers', 'medalBobDragons', 'BattlePassCommonPr_1',
 'march20', 'bootcampMedal', 'TenYearsCountdownParticipation', 'se2020Medal', 'june20',
 'BattlePassCommonPr_2', 'TenYearsCountdownSPGEventMedal', 'TenYearsCountdownBrawlMedal',
 'dedicationMedal1', 'dedicationMedal2', 'dedicationMedal3', 'dedicationMedal4',
 'betaTester_cn', 'BigAnniversaryMedal_CN', 'september20', 'BattlePassCommonPr_3',
 'hw2019Medal', 'hw2019Medal1', 'hw2019Medal2', 'hw2019Medal3', 'october20',
 'NY21_AtmsphrLevel', 'NY21_CelebChallenge', 'january21',
 'bob2021Lebwa_ru', 'bob2021Yusha_ru', 'bob2021Amway921_ru', 'bob2021KorbenDallas_ru',
 'bob2021NearYou_ru', 'bob2021EvilGranny_ru', 'bob2021Vspishka_ru', 'bob2021Inspirer_ru',
 'bob2021Circon_eu', 'bob2021Dakillzor_eu', 'bob2021NewMulti2k_eu', 'bob2021Orzanel_eu',
 'bob2021Cabbagemechanic_na', 'bob2021TragicLoss_na', 'bob2021CmdrAF_na',
 'bob2021MasterTortoise_apac', 'bob2021SummerTiger_apac', 'bob2021Maharlika_apac',
 'february21', 'BattlePassCommonPr_4', 'march21', 'april21', 'gagarin21', 'may21',
 'june21', 'BattlePassCommonPr_5', 'mapboxSeason1', 'mapboxSeason2', 'mapboxSeason3',
 'july21', 'august21', 'BattlePassCommonPr_6', 'september21', 'october21',
 'hw2021Medal1', 'hw2021Medal2', 'november21', '11YearsOfService',
 'NY22_AtmsphrLevel', 'NY22_CelebChallenge', 'december21', 'BattlePassCommonPr_7',
 'oowCBTParticipant', 'june22', 'BattlePassCommonPr_8', 'BattlePassCommonPr_8ru',
 'BattlePassCommonPr_8quest', 'july22', 'BattlePassCommonPr_9',
 'prime_gaming_reserved_1', 'prime_gaming_reserved_2', 'prime_gaming_reserved_3',
 'prime_gaming_reserved_4', 'prime_gaming_reserved_5', 'prime_gaming_reserved_6',
 'prime_gaming_reserved_7', 'prime_gaming_reserved_8', 'prime_gaming_reserved_9',
 'prime_gaming_reserved_10', 'prime_gaming_reserved_11', 'prime_gaming_reserved_12']
_singleAchievementsPopUps = [
 'titleSniper', 'invincible', 'diehard', 'handOfDeath',
 'armorPiercer', 'battleCitizen', 'WFC2014', 'tacticalBreakthrough', 'aimer',
 'deathTrack', 'firstMerit', 'tankwomen', 'operationWinter', 'victoryMarch', 'fallout',
 'fallout2', 'falloutSingleWolf', 'falloutPackOfWolfs', 'falloutSteelHunter',
 'falloutAlwaysInLine', 'moonSphere', 'EFC2016', 'markIProtector', 'markIBaseProtector',
 'xmasTreeBronze', 'xmasTreeSilver', 'xmasTreeGold', 'rankedBattlesPioneer',
 'HE17A1', 'HE17A2', 'HE17A3', 'NY18A1', 'NY18A2', 'NY18A3',
 'rankedBattlesHero', 'rankedBattlesSeasonOne',
 'FE18Universal', 'FE18Collection1', 'FE18Collection2', 'FE18Collection3',
 'FE18OpenRegistration', 'FE18OpenPlayOff', 'FE18OpenFinalStage', 'FE18OpenFirstPlace',
 'medalKursk', 'newMeritPM2', 'streamersEventUsha', 'streamersEventJove',
 'streamersEventAmway921', 'streamersEventLeBwA', 'twitchPrime',
 'alphaTester', 'betaTester', '10YearsOfService', '09YearsOfService', '08YearsOfService',
 '07YearsOfService', '06YearsOfService', '05YearsOfService', '04YearsOfService',
 '03YearsOfService', '02YearsOfService', '01YearsOfService', 'NY19A1',
 'NY19A2', 'NY19A3', 'epicBattle1', 'epicBattle2', 'epicBattle3', 'epicBattle4',
 'DdaymarathonMedal', 'twitchPrime2', 'twitchPrime3', 'se12019Medal',
 'Fest19Collection1', 'Fest19Collection2', 'Fest19Collection3', 'twitchPrime4',
 'BR2019Title25', 'BR2019Title15', 'BR2019Title5', 'october19',
 'Fest19Offspring', 'Fest19Racer', 'november19', 'december19', 'NY20A1', 'NY20A2',
 'NY20A3', 'january20', 'february20', 'medalBobLebwa', 'medalBobYusha',
 'medalBobAmway921', 'medalBobKorbenDallas', 'medalBobMailand', 'medalBobSkill4ltu',
 'medalBobDezgamez', 'medalBobAwesomeEpicGuys', 'medalBobTigers', 'medalBobDragons',
 'BattlePassCommonPr_1', 'march20', 'bootcampMedal', 'TenYearsCountdownParticipation',
 'se2020Medal', 'june20', 'BattlePassCommonPr_2', 'TenYearsCountdownSPGEventMedal',
 'TenYearsCountdownBrawlMedal', 'betaTester_cn', 'BigAnniversaryMedal_CN', 'september20',
 'BattlePassCommonPr_3', 'hw2019Medal', 'hw2019Medal1', 'hw2019Medal2', 'hw2019Medal3',
 'october20', 'NY21_AtmsphrLevel', 'NY21_CelebChallenge', 'january21',
 'bob2021Lebwa_ru', 'bob2021Yusha_ru', 'bob2021Amway921_ru',
 'bob2021KorbenDallas_ru', 'bob2021NearYou_ru', 'bob2021EvilGranny_ru',
 'bob2021Vspishka_ru', 'bob2021Inspirer_ru', 'bob2021Circon_eu', 'bob2021Dakillzor_eu',
 'bob2021NewMulti2k_eu', 'bob2021Orzanel_eu', 'bob2021Cabbagemechanic_na',
 'bob2021TragicLoss_na', 'bob2021CmdrAF_na', 'bob2021MasterTortoise_apac',
 'bob2021SummerTiger_apac', 'bob2021Maharlika_apac', 'february21', 'BattlePassCommonPr_4',
 'march21', 'april21', 'gagarin21', 'may21', 'june21', 'BattlePassCommonPr_5',
 'mapboxSeason1', 'mapboxSeason2', 'mapboxSeason3', 'july21', 'august21',
 'BattlePassCommonPr_6', 'september21', 'october21', 'hw2021Medal1', 'hw2021Medal2',
 'november21', '11YearsOfService', 'NY22_AtmsphrLevel', 'NY22_CelebChallenge',
 'december21', 'BattlePassCommonPr_7', 'oowCBTParticipant', 'june22',
 'BattlePassCommonPr_8', 'BattlePassCommonPr_8ru', 'BattlePassCommonPr_8quest', 'july22',
 'BattlePassCommonPr_9', 'prime_gaming_reserved_1', 'prime_gaming_reserved_2',
 'prime_gaming_reserved_3', 'prime_gaming_reserved_4', 'prime_gaming_reserved_5',
 'prime_gaming_reserved_6', 'prime_gaming_reserved_7', 'prime_gaming_reserved_8',
 'prime_gaming_reserved_9', 'prime_gaming_reserved_10', 'prime_gaming_reserved_11',
 'prime_gaming_reserved_12']
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder('singleAchievements', _SINGLE_ACHIEVEMENTS_VALUES, SINGLE_ACHIEVEMENTS_DEPENDENCIES, _singleAchievementsPopUps)
FORT_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'conqueror', 'fireAndSword', 'crusher', 'counterblow', 'kampfer', 'soldierOfFortune']
_fortPersonalAchievementsPopUps = [
 'soldierOfFortune']
_fortPersonalAchievementsBlockBuilder = StaticSizeBlockBuilder('fortAchievements', FORT_ACHIEVEMENTS_BLOCK_LAYOUT, FORT_ACHIEVEMENTS_DEPENDENCIES, _fortPersonalAchievementsPopUps)
CLAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'medalRotmistrov']
_clanAchievementsPopUps = ['medalRotmistrov']
_clanAchievementsBlockBuilder = StaticSizeBlockBuilder('clanAchievements', CLAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _clanAchievementsPopUps)
RANKED_BADGES_BLOCK_LAYOUT = [
 '1', '2', '3', '4', '5', '6', '7', '8', '9']
_playerBadgesBlockBuilder = DictBlockBuilder('playerBadges', 'I', 'I', {})
_rankedSeasonsBlockBuilder = DictBlockBuilder('rankedSeasons', 'II', 'BHHHH', {})
_rareAchievementsBlockBuilder = ListBlockBuilder('rareAchievements', 'I', {})
UNIQUE_ACHIEVEMENT_VALUES = [
 'histBattle1_battlefield', 'histBattle1_historyLessons',
 'histBattle2_battlefield', 'histBattle2_historyLessons',
 'histBattle3_battlefield', 'histBattle3_historyLessons',
 'histBattle4_battlefield', 'histBattle4_historyLessons',
 'histBattle5_battlefield', 'histBattle5_historyLessons',
 'histBattle6_battlefield', 'histBattle6_historyLessons']
_uniqueAchievementPopUps = [
 'histBattle1_battlefield', 'histBattle1_historyLessons',
 'histBattle2_battlefield', 'histBattle2_historyLessons',
 'histBattle3_battlefield', 'histBattle3_historyLessons',
 'histBattle4_battlefield', 'histBattle4_historyLessons',
 'histBattle5_battlefield', 'histBattle5_historyLessons',
 'histBattle6_battlefield', 'histBattle6_historyLessons']
_uniqueAchievementBlockBuilder = BinarySetDossierBlockBuilder('uniqueAchievements', UNIQUE_ACHIEVEMENT_VALUES, {}, _uniqueAchievementPopUps)
FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'shoulderToShoulder', 'aloneInTheField', 'fallenFlags', 'effectiveSupport',
 'stormLord', 'winnerLaurels', 'predator', 'unreachable', 'champion', 'bannerman',
 'falloutDieHard', 'deleted']
_falloutAchievementsPopUps = ['shoulderToShoulder', 'aloneInTheField', 'fallenFlags', 'effectiveSupport', 'stormLord',
 'winnerLaurels', 'predator', 'unreachable', 'champion', 'bannerman', 'falloutDieHard']
_falloutAchievementsBlockBuilder = StaticSizeBlockBuilder('falloutAchievements', FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT, {}, _falloutAchievementsPopUps)
EPIC_BATTLE_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'occupyingForce', 'ironShield', 'generalOfTheArmy', 'supremeGun',
 'smallArmy', 'frontlineMedal']
_epicBattleAchievementsPopUps = ['frontlineMedal']
_epicBattleAchievementsBlockBuilder = StaticSizeBlockBuilder('epicBattleAchievements', EPIC_BATTLE_ACHIEVEMENTS_BLOCK_LAYOUT, EPIC_BATTLE_STATS_DEPENDENCIES, _epicBattleAchievementsPopUps)
_epicBattleSeasonsBlockBuilder = DictBlockBuilder('epicSeasons', 'II', 'HHBHH', {})
_battleRoyaleSeasonsBlockBuilder = DictBlockBuilder('battleRoyaleSeasons', 'II', 'HHH', {})
accountDossierLayout = (
 _a15x15BlockBuilder, _a15x15_2BlockBuilder, _clanBlockBuilder,
 _clan2BlockBuilder, _companyBlockBuilder, _company2BlockBuilder, _a7x7BlockBuilder,
 _achievements15x15BlockBuilder, _vehTypeFragsBlockBuilder, _a15x15CutBlockBuilder,
 _rareAchievementsBlockBuilder, _totalBlockBuilder, _a7x7CutBlockBuilder,
 _max15x15BlockBuilder, _max7x7BlockBuilder,
 _achievements7x7BlockBuilder, _historicalBlockBuilder, _maxHistoricalBlockBuilder,
 _historicalAchievementsBlockBuilder, _historicalCutBlockBuilder,
 _uniqueAchievementBlockBuilder,
 _fortBattlesBlockBuilder, _maxFortBattlesBlockBuilder, _fortBattlesCutBlockBuilder,
 _fortSortiesBlockBuilder, _maxFortSortiesBlockBuilder, _fortSortiesCutBlockBuilder,
 _fortBattlesInClanBlockBuilder, _maxFortBattlesInClanBlockBuilder,
 _fortSortiesInClanBlockBuilder,
 _maxFortSortiesInClanBlockBuilder, _fortPersonalAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder, _clanAchievementsBlockBuilder,
 _rated7x7BlockBuilder, _maxRated7x7BlockBuilder, _achievementsRated7x7BlockBuilder,
 _rated7x7CutBlockBuilder,
 _globalMapMiddleBlockBuilder, _globalMapChampionBlockBuilder, _globalMapAbsoluteBlockBuilder,
 _maxGlobalMapMiddleBlockBuilder, _maxGlobalMapChampionBlockBuilder,
 _maxGlobalMapAbsoluteBlockBuilder,
 _globalMapCommonCutBlockBuilder,
 _falloutBlockBuilder, _falloutCutBlockBuilder, _maxFalloutBlockBuilder,
 _falloutAchievementsBlockBuilder,
 _rankedBlockBuilder, _maxRankedBlockBuilder, _rankedCutBlockBuilder,
 _rankedSeasonsBlockBuilder,
 _a30x30BlockBuilder, _a30x30CutBlockBuilder, _max30x30BlockBuilder, _markOfMasteryCut,
 _playerBadgesBlockBuilder,
 _epicBattleBlockBuilder, _epicBattleCutBlockBuilder, _maxEpicBattleBlockBuilder,
 _epicBattleAchievementsBlockBuilder, _rankedSeason1BlockBuilder, _rankedSeason2BlockBuilder,
 _rankedSeason3BlockBuilder, _maxRankedSeason1BlockBuilder, _maxRankedSeason2BlockBuilder,
 _maxRankedSeason3BlockBuilder, _rankedCutSeason1BlockBuilder, _rankedCutSeason2BlockBuilder,
 _rankedCutSeason3BlockBuilder, _rankedArchiveBlockBuilder, _maxRankedArchiveBlockBuilder,
 _rankedCutArchiveBlockBuilder, _epicBattleSeasonsBlockBuilder,
 _battleRoyaleSeasonsBlockBuilder, _ranked_10x10BlockBuilder, _maxRanked_10x10BlockBuilder,
 _rankedCut10x10BlockBuilder, _steamAchievementsBlockBuilder)
ACCOUNT_DOSSIER_BLOCKS = {b.name:b for b in accountDossierLayout}
ACCOUNT_DOSSIER_STATIC_BLOCKS = frozenset(b.name for b in accountDossierLayout if type(b) == StaticSizeBlockBuilder)
ACCOUNT_DOSSIER_BINARY_SET_BLOCKS = [ b.name for b in accountDossierLayout if type(b) == BinarySetDossierBlockBuilder ]
ACCOUNT_DOSSIER_DICT_BLOCKS = [ b.name for b in accountDossierLayout if type(b) == DictBlockBuilder ]
ACCOUNT_DOSSIER_LIST_BLOCKS = [ b.name for b in accountDossierLayout if type(b) == ListBlockBuilder ]