from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(104493)
    _tutorialInitialLoop = DynAccessor(104494)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(104495)
        up_particles = DynAccessor(104496)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(104497)
            crewCommander = DynAccessor(104498)
            crewDriver = DynAccessor(104499)
            crewGunner = DynAccessor(104500)
            crewLoader = DynAccessor(104501)
            crewRadioOperator = DynAccessor(104502)
            skillAdrenalineRush = DynAccessor(104503)
            skillArmorer = DynAccessor(104504)
            skillArtLamp = DynAccessor(104505)
            skillBrothersInArms = DynAccessor(104506)
            skillCallForVengeance = DynAccessor(104507)
            skillClutchBraking = DynAccessor(104508)
            skillCommanderBonus = DynAccessor(104509)
            skillConcealment = DynAccessor(104510)
            skillControlledImpact = DynAccessor(104511)
            skillDeadEye = DynAccessor(104512)
            skillDesignatedTarget = DynAccessor(104513)
            skillEagleEye = DynAccessor(104514)
            skillExpert = DynAccessor(104515)
            skillFirefighting = DynAccessor(104516)
            skillIntuition = DynAccessor(104517)
            skillJackOfAllTrades = DynAccessor(104518)
            skillMentor = DynAccessor(104519)
            skillOffRoadDriving = DynAccessor(104520)
            skillPreventativeMaintenance = DynAccessor(104521)
            skillRelaying = DynAccessor(104522)
            skillRepairs = DynAccessor(104523)
            skillSafeStowage = DynAccessor(104524)
            skillSignalBoosting = DynAccessor(104525)
            skillSituationalAwareness = DynAccessor(104526)
            skillSixthSense = DynAccessor(104527)
            skillSmoothRide = DynAccessor(104528)
            skillSnapShot = DynAccessor(104529)
            skillSniper = DynAccessor(104530)
            skillSoundIntelligence = DynAccessor(104531)
            statConcealment = DynAccessor(104532)
            statFirepower = DynAccessor(104533)
            statMobility = DynAccessor(104534)
            statSpotting = DynAccessor(104535)
            statSurvivability = DynAccessor(104536)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(104537)
        ay_gun = DynAccessor(104538)
        ay_tracks = DynAccessor(104539)
        ay_turret = DynAccessor(104540)
        video_reward = DynAccessor(104541)
        video_reward_min = DynAccessor(104542)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(104543)
        v_182_0 = DynAccessor(104544)
        v_183_0 = DynAccessor(104545)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(104546)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(104547)
            overcharge = DynAccessor(104548)
            power_shot = DynAccessor(104549)
            rapid_shelling = DynAccessor(104550)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(104551)
            Loop_1 = DynAccessor(104552)
            Loop_10 = DynAccessor(104553)
            Loop_2 = DynAccessor(104554)
            Loop_3 = DynAccessor(104555)
            Loop_4 = DynAccessor(104556)
            Loop_5 = DynAccessor(104557)
            Loop_6 = DynAccessor(104558)
            Loop_7 = DynAccessor(104559)
            Loop_8 = DynAccessor(104560)
            Loop_9 = DynAccessor(104561)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(104562)
        example_2 = DynAccessor(104563)
        example_3 = DynAccessor(104564)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(104565)
            gold = DynAccessor(104566)
            silver = DynAccessor(104567)
            standart = DynAccessor(104568)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(104569)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104570)
            small = DynAccessor(104571)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104572)
            standart = DynAccessor(104573)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104574)
            standart = DynAccessor(104575)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104576)
            standart = DynAccessor(104577)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(104578)
            mtl_1_35 = DynAccessor(104579)
            mt_drops = DynAccessor(104580)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104581)
            medium = DynAccessor(104582)
            small = DynAccessor(104583)
            tanks_6 = DynAccessor(104584)
            tanks_7 = DynAccessor(104585)
            tanks_8 = DynAccessor(104586)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(104587)
            G171_E77 = DynAccessor(104588)
            G171_E77_02 = DynAccessor(104589)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(104590)
            intro = DynAccessor(104591)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(104592)
            Pl35_CS_57_Sokol = DynAccessor(104593)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(104594)
        operation_10 = DynAccessor(104595)
        operation_8 = DynAccessor(104596)
        operation_9 = DynAccessor(104597)
        operation_99 = DynAccessor(104598)
        video_operations_person = DynAccessor(104599)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(104600)

    platoon = _platoon()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro = DynAccessor(104601)
        portal_outro = DynAccessor(104602)

        class _abilities(DynAccessor):
            __slots__ = ()
            berserk_portal = DynAccessor(104603)
            curse_shot_portal = DynAccessor(104604)
            fire_shot_portal = DynAccessor(104605)
            frozen_shot_portal = DynAccessor(104606)
            guided_missile_portal = DynAccessor(104607)
            laugh_shot_portal = DynAccessor(104608)
            minefield_portal = DynAccessor(104609)
            reload_aura_portal = DynAccessor(104610)
            sentry_gun_portal = DynAccessor(104611)
            shield_portal = DynAccessor(104612)
            trap_portal = DynAccessor(104613)
            vehicle_change_shot_portal = DynAccessor(104614)

        abilities = _abilities()

    portal = _portal()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(104615)

    vehicle = _vehicle()