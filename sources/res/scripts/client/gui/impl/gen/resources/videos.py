from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(117469)
    _tutorialInitialLoop = DynAccessor(117470)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(117471)
        up_particles = DynAccessor(117472)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(117473)
            crewCommander = DynAccessor(117474)
            crewDriver = DynAccessor(117475)
            crewGunner = DynAccessor(117476)
            crewLoader = DynAccessor(117477)
            crewRadioOperator = DynAccessor(117478)
            skillAdrenalineRush = DynAccessor(117479)
            skillArmorer = DynAccessor(117480)
            skillArtLamp = DynAccessor(117481)
            skillBrothersInArms = DynAccessor(117482)
            skillCallForVengeance = DynAccessor(117483)
            skillClutchBraking = DynAccessor(117484)
            skillCommanderBonus = DynAccessor(117485)
            skillConcealment = DynAccessor(117486)
            skillControlledImpact = DynAccessor(117487)
            skillDeadEye = DynAccessor(117488)
            skillDesignatedTarget = DynAccessor(117489)
            skillEagleEye = DynAccessor(117490)
            skillExpert = DynAccessor(117491)
            skillFirefighting = DynAccessor(117492)
            skillIntuition = DynAccessor(117493)
            skillJackOfAllTrades = DynAccessor(117494)
            skillMentor = DynAccessor(117495)
            skillOffRoadDriving = DynAccessor(117496)
            skillPreventativeMaintenance = DynAccessor(117497)
            skillRelaying = DynAccessor(117498)
            skillRepairs = DynAccessor(117499)
            skillSafeStowage = DynAccessor(117500)
            skillSignalBoosting = DynAccessor(117501)
            skillSituationalAwareness = DynAccessor(117502)
            skillSixthSense = DynAccessor(117503)
            skillSmoothRide = DynAccessor(117504)
            skillSnapShot = DynAccessor(117505)
            skillSniper = DynAccessor(117506)
            skillSoundIntelligence = DynAccessor(117507)
            statConcealment = DynAccessor(117508)
            statFirepower = DynAccessor(117509)
            statMobility = DynAccessor(117510)
            statSpotting = DynAccessor(117511)
            statSurvivability = DynAccessor(117512)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(117513)
        ay_gun = DynAccessor(117514)
        ay_tracks = DynAccessor(117515)
        ay_turret = DynAccessor(117516)
        video_reward = DynAccessor(117517)
        video_reward_min = DynAccessor(117518)

    armory_yard = _armory_yard()

    class _battleContextHints(DynAccessor):
        __slots__ = ()
        AmmoTypeAvailable = DynAccessor(117519)
        AmmunitionCrit = DynAccessor(117520)
        FueltankCrit = DynAccessor(117521)
        InSafetyWhileNotObserved = DynAccessor(117522)
        KilledWhileObserved = DynAccessor(117523)
        ModuleDamage = DynAccessor(117524)

    battleContextHints = _battleContextHints()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_211_0 = DynAccessor(117525)
        v_212_0 = DynAccessor(117526)
        v_213_0 = DynAccessor(117527)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(117528)
        Intro = DynAccessor(117529)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(117530)
            overcharge = DynAccessor(117531)
            power_shot = DynAccessor(117532)
            teleport = DynAccessor(117533)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(117534)

        progression = _progression()

    cosmic = _cosmic()

    class _customizationResource(DynAccessor):
        __slots__ = ()
        cr_paint_reward = DynAccessor(117535)

    customizationResource = _customizationResource()

    class _development(DynAccessor):
        __slots__ = ()
        cosmic_intro_vp8_8_128 = DynAccessor(117536)
        cosmic_intro_vp8_8_256 = DynAccessor(117537)
        cosmic_intro_vp8_8_96 = DynAccessor(117538)
        cosmic_intro_vp9_8_128 = DynAccessor(117539)
        cosmic_intro_vp9_8_256 = DynAccessor(117540)
        cosmic_intro_vp9_8_96 = DynAccessor(117541)
        example = DynAccessor(117542)
        example_2 = DynAccessor(117543)
        example_3 = DynAccessor(117544)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()
        bg_unique = DynAccessor(117545)

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(117546)
            gold = DynAccessor(117547)
            silver = DynAccessor(117548)
            standart = DynAccessor(117549)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(117550)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117551)
            small = DynAccessor(117552)

        bd2025 = _bd2025()

        class _bd2026(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117553)
            small = DynAccessor(117554)

        bd2026 = _bd2026()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117555)
            standart = DynAccessor(117556)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117557)
            standart = DynAccessor(117558)

        cosmic2025 = _cosmic2025()

        class _cosmic2026(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117559)
            standart = DynAccessor(117560)

        cosmic2026 = _cosmic2026()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(117561)
            standart = DynAccessor(117562)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(117563)
            mtl_1_35 = DynAccessor(117564)
            mtl_1_43 = DynAccessor(117565)
            mt_drops = DynAccessor(117566)

        mt_lootbox = _mt_lootbox()

        class _ny2027(DynAccessor):
            __slots__ = ()
            ny_2027_big = DynAccessor(117567)
            ny_2027_small = DynAccessor(117568)
            ny_2027_tanks = DynAccessor(117569)

        ny2027 = _ny2027()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(117570)
            medium = DynAccessor(117571)
            small = DynAccessor(117572)
            tanks_6 = DynAccessor(117573)
            tanks_7 = DynAccessor(117574)
            tanks_8 = DynAccessor(117575)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _common(DynAccessor):
            __slots__ = ()
            J27_O_I_120_BP = DynAccessor(117576)
            R149_Object_268_4_02 = DynAccessor(117577)
            R177_ISU_152K_BL10_02 = DynAccessor(117578)
            R248_T44_Storm = DynAccessor(117579)
            R45_IS_7_02 = DynAccessor(117580)
            Un24_Vz_68_2_Britva = DynAccessor(117581)

        common = _common()

        class _cosmic_2026(DynAccessor):
            __slots__ = ()
            G171_E77_02 = DynAccessor(117582)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(117583)
            intro = DynAccessor(117584)
            R239_ST_Molot_02 = DynAccessor(117585)

        cosmic_2026 = _cosmic_2026()

        class _cosmic_2026_2(DynAccessor):
            __slots__ = ()
            F131_Coutelas = DynAccessor(117586)
            GB141_Celestial_2_51 = DynAccessor(117587)
            intro = DynAccessor(117588)
            R239_ST_Molot = DynAccessor(117589)

        cosmic_2026_2 = _cosmic_2026_2()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            A122_TS_5 = DynAccessor(117590)
            Ch46_113_140 = DynAccessor(117591)
            G164_Kpz_Pr_68_P = DynAccessor(117592)
            Pl35_CS_57_Sokol = DynAccessor(117593)
            R121_KV4_KTT = DynAccessor(117594)
            S22_Strv_S1 = DynAccessor(117595)

        mtl_universal = _mtl_universal()

        class _ny_2027_big(DynAccessor):
            __slots__ = ()
            A165_XM57 = DynAccessor(117596)
            A175_OTAC_MT_58 = DynAccessor(117597)
            A175_OTAC_MT_58_02 = DynAccessor(117598)
            customizations_177484 = DynAccessor(117599)
            customizations_7990860 = DynAccessor(117600)
            customizations_7999308 = DynAccessor(117601)
            customizations_7999564 = DynAccessor(117602)
            customizations_8001356 = DynAccessor(117603)
            customizations_8001612 = DynAccessor(117604)
            Cz39_SD_122_49_Sekera = DynAccessor(117605)
            F118_Char_Mle_75 = DynAccessor(117606)
            G181_StuG_Maus_17cm = DynAccessor(117607)
            G196_E_75_Ausf_B_Doppel = DynAccessor(117608)
            GB139_Vulcan = DynAccessor(117609)
            intro = DynAccessor(117610)
            It33_Orso = DynAccessor(117611)
            ny_2027_tanks = DynAccessor(117612)
            R165_Object_703_II_100 = DynAccessor(117613)
            R222_Object_120_Taran = DynAccessor(117614)
            R223_T_54B_1958 = DynAccessor(117615)
            R228_Duplet = DynAccessor(117616)

        ny_2027_big = _ny_2027_big()

        class _ny_2027_tanks(DynAccessor):
            __slots__ = ()
            A115_Chrysler_K = DynAccessor(117617)
            A117_T26E5 = DynAccessor(117618)
            A124_T54E2 = DynAccessor(117619)
            A136_T42 = DynAccessor(117620)
            A140_ASTRON_REX_105mm = DynAccessor(117621)
            G120_M41_90 = DynAccessor(117622)
            G138_VK168_02 = DynAccessor(117623)
            G44_JagdTigerH = DynAccessor(117624)
            GB115_Gonsalo = DynAccessor(117625)
            GB121_GSOR_1010_FB = DynAccessor(117626)
            GB87_Chieftain_T95_turret = DynAccessor(117627)
            It18_Progetto_C45_mod_71 = DynAccessor(117628)
            Pl08_50TP_prototyp = DynAccessor(117629)
            R134_Object_252U = DynAccessor(117630)
            R146_STG = DynAccessor(117631)
            R188_Object_259A = DynAccessor(117632)
            S25_EMIL_51 = DynAccessor(117633)
            S26_Lansen_C = DynAccessor(117634)

        ny_2027_tanks = _ny_2027_tanks()

    lootbox_reward_video = _lootbox_reward_video()

    class _mt_birthday(DynAccessor):
        __slots__ = ()

        class _tankMail(DynAccessor):
            __slots__ = ()
            sentGift = DynAccessor(117635)

        tankMail = _tankMail()

    mt_birthday = _mt_birthday()

    class _newbie_start_page(DynAccessor):
        __slots__ = ()
        option_1 = DynAccessor(117636)
        option_2 = DynAccessor(117637)
        option_3 = DynAccessor(117638)

    newbie_start_page = _newbie_start_page()

    class _new_year(DynAccessor):
        __slots__ = ()

        class _clips(DynAccessor):
            __slots__ = ()
            clip_1 = DynAccessor(117639)
            clip_2 = DynAccessor(117640)
            ldt_reward = DynAccessor(117641)

        clips = _clips()

        class _greetings(DynAccessor):
            __slots__ = ()
            lvl_greetings = DynAccessor(117642)
            ng_greetings = DynAccessor(117643)
            report_1 = DynAccessor(117644)
            report_2 = DynAccessor(117645)
            report_3 = DynAccessor(117646)
            report_4 = DynAccessor(117647)
            report_5 = DynAccessor(117648)
            report_6 = DynAccessor(117649)
            report_7 = DynAccessor(117650)

        greetings = _greetings()

        class _lootbox(DynAccessor):
            __slots__ = ()
            box_delivery = DynAccessor(117651)
            pre_delivery = DynAccessor(117652)

        lootbox = _lootbox()

        class _onboarding(DynAccessor):
            __slots__ = ()
            onboarding_day = DynAccessor(117653)
            onboarding_night = DynAccessor(117654)

        onboarding = _onboarding()

        class _petTvScreen(DynAccessor):
            __slots__ = ()
            animations = DynAccessor(117655)

        petTvScreen = _petTvScreen()

        class _robotTvScreen(DynAccessor):
            __slots__ = ()
            tv_screen_active = DynAccessor(117656)
            tv_screen_idle = DynAccessor(117657)

        robotTvScreen = _robotTvScreen()

    new_year = _new_year()

    class _paragons(DynAccessor):
        __slots__ = ()
        A150_MBT_B = DynAccessor(117658)
        Ch57_BZT_70 = DynAccessor(117659)
        F134_ARL_Projet_F = DynAccessor(117660)
        G184_EisBaer = DynAccessor(117661)
        GB140_Champion = DynAccessor(117662)
        R124_Object_279 = DynAccessor(117663)

    paragons = _paragons()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(117664)
        operation_10 = DynAccessor(117665)
        operation_8 = DynAccessor(117666)
        operation_9 = DynAccessor(117667)
        operation_99 = DynAccessor(117668)
        video_operations_person = DynAccessor(117669)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(117670)

    platoon = _platoon()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(117671)

    vehicle = _vehicle()