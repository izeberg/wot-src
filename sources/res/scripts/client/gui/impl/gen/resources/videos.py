from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(104494)
    _tutorialInitialLoop = DynAccessor(104495)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(104496)
        up_particles = DynAccessor(104497)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(104498)
            crewCommander = DynAccessor(104499)
            crewDriver = DynAccessor(104500)
            crewGunner = DynAccessor(104501)
            crewLoader = DynAccessor(104502)
            crewRadioOperator = DynAccessor(104503)
            skillAdrenalineRush = DynAccessor(104504)
            skillArmorer = DynAccessor(104505)
            skillArtLamp = DynAccessor(104506)
            skillBrothersInArms = DynAccessor(104507)
            skillCallForVengeance = DynAccessor(104508)
            skillClutchBraking = DynAccessor(104509)
            skillCommanderBonus = DynAccessor(104510)
            skillConcealment = DynAccessor(104511)
            skillControlledImpact = DynAccessor(104512)
            skillDeadEye = DynAccessor(104513)
            skillDesignatedTarget = DynAccessor(104514)
            skillEagleEye = DynAccessor(104515)
            skillExpert = DynAccessor(104516)
            skillFirefighting = DynAccessor(104517)
            skillIntuition = DynAccessor(104518)
            skillJackOfAllTrades = DynAccessor(104519)
            skillMentor = DynAccessor(104520)
            skillOffRoadDriving = DynAccessor(104521)
            skillPreventativeMaintenance = DynAccessor(104522)
            skillRelaying = DynAccessor(104523)
            skillRepairs = DynAccessor(104524)
            skillSafeStowage = DynAccessor(104525)
            skillSignalBoosting = DynAccessor(104526)
            skillSituationalAwareness = DynAccessor(104527)
            skillSixthSense = DynAccessor(104528)
            skillSmoothRide = DynAccessor(104529)
            skillSnapShot = DynAccessor(104530)
            skillSniper = DynAccessor(104531)
            skillSoundIntelligence = DynAccessor(104532)
            statConcealment = DynAccessor(104533)
            statFirepower = DynAccessor(104534)
            statMobility = DynAccessor(104535)
            statSpotting = DynAccessor(104536)
            statSurvivability = DynAccessor(104537)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(104538)
        ay_gun = DynAccessor(104539)
        ay_tracks = DynAccessor(104540)
        ay_turret = DynAccessor(104541)
        video_reward = DynAccessor(104542)
        video_reward_min = DynAccessor(104543)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(104544)
        v_182_0 = DynAccessor(104545)
        v_183_0 = DynAccessor(104546)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(104547)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(104548)
            overcharge = DynAccessor(104549)
            power_shot = DynAccessor(104550)
            rapid_shelling = DynAccessor(104551)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(104552)
            Loop_1 = DynAccessor(104553)
            Loop_10 = DynAccessor(104554)
            Loop_2 = DynAccessor(104555)
            Loop_3 = DynAccessor(104556)
            Loop_4 = DynAccessor(104557)
            Loop_5 = DynAccessor(104558)
            Loop_6 = DynAccessor(104559)
            Loop_7 = DynAccessor(104560)
            Loop_8 = DynAccessor(104561)
            Loop_9 = DynAccessor(104562)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(104563)
        example_2 = DynAccessor(104564)
        example_3 = DynAccessor(104565)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(104566)
            gold = DynAccessor(104567)
            silver = DynAccessor(104568)
            standart = DynAccessor(104569)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(104570)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104571)
            small = DynAccessor(104572)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104573)
            standart = DynAccessor(104574)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104575)
            standart = DynAccessor(104576)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104577)
            standart = DynAccessor(104578)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(104579)
            mtl_1_35 = DynAccessor(104580)
            mt_drops = DynAccessor(104581)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104582)
            medium = DynAccessor(104583)
            small = DynAccessor(104584)
            tanks_6 = DynAccessor(104585)
            tanks_7 = DynAccessor(104586)
            tanks_8 = DynAccessor(104587)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(104588)
            G171_E77 = DynAccessor(104589)
            G171_E77_02 = DynAccessor(104590)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(104591)
            intro = DynAccessor(104592)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(104593)
            Pl35_CS_57_Sokol = DynAccessor(104594)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(104595)
        operation_10 = DynAccessor(104596)
        operation_8 = DynAccessor(104597)
        operation_9 = DynAccessor(104598)
        operation_99 = DynAccessor(104599)
        video_operations_person = DynAccessor(104600)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(104601)

    platoon = _platoon()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro = DynAccessor(104602)
        portal_outro = DynAccessor(104603)

        class _abilities(DynAccessor):
            __slots__ = ()
            berserk_portal = DynAccessor(104604)
            curse_shot_portal = DynAccessor(104605)
            fire_shot_portal = DynAccessor(104606)
            frozen_shot_portal = DynAccessor(104607)
            guided_missile_portal = DynAccessor(104608)
            laugh_shot_portal = DynAccessor(104609)
            minefield_portal = DynAccessor(104610)
            reload_aura_portal = DynAccessor(104611)
            sentry_gun_portal = DynAccessor(104612)
            shield_portal = DynAccessor(104613)
            trap_portal = DynAccessor(104614)
            vehicle_change_shot_portal = DynAccessor(104615)

        abilities = _abilities()

    portal = _portal()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(104616)

    vehicle = _vehicle()