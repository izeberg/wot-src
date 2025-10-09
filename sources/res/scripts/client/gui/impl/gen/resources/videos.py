from gui.impl.gen_utils import DynAccessor

class Videos(DynAccessor):
    __slots__ = ()
    _tutorialInitial = DynAccessor(104578)
    _tutorialInitialLoop = DynAccessor(104579)

    class _achievements(DynAccessor):
        __slots__ = ()
        particles = DynAccessor(104580)
        up_particles = DynAccessor(104581)

    achievements = _achievements()

    class _animations(DynAccessor):
        __slots__ = ()

        class _advancedHints(DynAccessor):
            __slots__ = ()
            abilityPreview = DynAccessor(104582)
            crewCommander = DynAccessor(104583)
            crewDriver = DynAccessor(104584)
            crewGunner = DynAccessor(104585)
            crewLoader = DynAccessor(104586)
            crewRadioOperator = DynAccessor(104587)
            skillAdrenalineRush = DynAccessor(104588)
            skillArmorer = DynAccessor(104589)
            skillArtLamp = DynAccessor(104590)
            skillBrothersInArms = DynAccessor(104591)
            skillCallForVengeance = DynAccessor(104592)
            skillClutchBraking = DynAccessor(104593)
            skillCommanderBonus = DynAccessor(104594)
            skillConcealment = DynAccessor(104595)
            skillControlledImpact = DynAccessor(104596)
            skillDeadEye = DynAccessor(104597)
            skillDesignatedTarget = DynAccessor(104598)
            skillEagleEye = DynAccessor(104599)
            skillExpert = DynAccessor(104600)
            skillFirefighting = DynAccessor(104601)
            skillIntuition = DynAccessor(104602)
            skillJackOfAllTrades = DynAccessor(104603)
            skillMentor = DynAccessor(104604)
            skillOffRoadDriving = DynAccessor(104605)
            skillPreventativeMaintenance = DynAccessor(104606)
            skillRelaying = DynAccessor(104607)
            skillRepairs = DynAccessor(104608)
            skillSafeStowage = DynAccessor(104609)
            skillSignalBoosting = DynAccessor(104610)
            skillSituationalAwareness = DynAccessor(104611)
            skillSixthSense = DynAccessor(104612)
            skillSmoothRide = DynAccessor(104613)
            skillSnapShot = DynAccessor(104614)
            skillSniper = DynAccessor(104615)
            skillSoundIntelligence = DynAccessor(104616)
            statConcealment = DynAccessor(104617)
            statFirepower = DynAccessor(104618)
            statMobility = DynAccessor(104619)
            statSpotting = DynAccessor(104620)
            statSurvivability = DynAccessor(104621)

        advancedHints = _advancedHints()

    animations = _animations()

    class _armory_yard(DynAccessor):
        __slots__ = ()
        ay_armour = DynAccessor(104622)
        ay_gun = DynAccessor(104623)
        ay_tracks = DynAccessor(104624)
        ay_turret = DynAccessor(104625)
        video_reward = DynAccessor(104626)
        video_reward_min = DynAccessor(104627)

    armory_yard = _armory_yard()

    class _battle_pass(DynAccessor):
        __slots__ = ()
        v_181_0 = DynAccessor(104628)
        v_182_0 = DynAccessor(104629)
        v_183_0 = DynAccessor(104630)

    battle_pass = _battle_pass()

    class _cosmic(DynAccessor):
        __slots__ = ()
        hyperjump = DynAccessor(104631)

        class _abilities(DynAccessor):
            __slots__ = ()
            black_hole = DynAccessor(104632)
            overcharge = DynAccessor(104633)
            power_shot = DynAccessor(104634)
            rapid_shelling = DynAccessor(104635)

        abilities = _abilities()

        class _progression(DynAccessor):
            __slots__ = ()
            Loop_0 = DynAccessor(104636)
            Loop_1 = DynAccessor(104637)
            Loop_10 = DynAccessor(104638)
            Loop_2 = DynAccessor(104639)
            Loop_3 = DynAccessor(104640)
            Loop_4 = DynAccessor(104641)
            Loop_5 = DynAccessor(104642)
            Loop_6 = DynAccessor(104643)
            Loop_7 = DynAccessor(104644)
            Loop_8 = DynAccessor(104645)
            Loop_9 = DynAccessor(104646)

        progression = _progression()

    cosmic = _cosmic()

    class _development(DynAccessor):
        __slots__ = ()
        example = DynAccessor(104647)
        example_2 = DynAccessor(104648)
        example_3 = DynAccessor(104649)

    development = _development()

    class _event_loot_boxes(DynAccessor):
        __slots__ = ()

        class _bd2023(DynAccessor):
            __slots__ = ()
            bronze = DynAccessor(104650)
            gold = DynAccessor(104651)
            silver = DynAccessor(104652)
            standart = DynAccessor(104653)

        bd2023 = _bd2023()

        class _bd2024(DynAccessor):
            __slots__ = ()
            lootbox = DynAccessor(104654)

        bd2024 = _bd2024()

        class _bd2025(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104655)
            small = DynAccessor(104656)

        bd2025 = _bd2025()

        class _cosmic2024(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104657)
            standart = DynAccessor(104658)

        cosmic2024 = _cosmic2024()

        class _cosmic2025(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104659)
            standart = DynAccessor(104660)

        cosmic2025 = _cosmic2025()

        class _hw2023(DynAccessor):
            __slots__ = ()
            silver = DynAccessor(104661)
            standart = DynAccessor(104662)

        hw2023 = _hw2023()

        class _mt_lootbox(DynAccessor):
            __slots__ = ()
            mtl_1_24 = DynAccessor(104663)
            mtl_1_35 = DynAccessor(104664)
            mt_drops = DynAccessor(104665)

        mt_lootbox = _mt_lootbox()

        class _rp_2024(DynAccessor):
            __slots__ = ()
            large = DynAccessor(104666)
            medium = DynAccessor(104667)
            small = DynAccessor(104668)
            tanks_6 = DynAccessor(104669)
            tanks_7 = DynAccessor(104670)
            tanks_8 = DynAccessor(104671)

        rp_2024 = _rp_2024()

    event_loot_boxes = _event_loot_boxes()

    class _lootbox_reward_video(DynAccessor):
        __slots__ = ()

        class _cosmic_2025(DynAccessor):
            __slots__ = ()
            Cz37_Vz_59_Dravec = DynAccessor(104672)
            G171_E77 = DynAccessor(104673)
            G171_E77_02 = DynAccessor(104674)
            GB110_FV4201_Chieftain_Prototype_B = DynAccessor(104675)
            intro = DynAccessor(104676)

        cosmic_2025 = _cosmic_2025()

        class _mtl_universal(DynAccessor):
            __slots__ = ()
            G164_Kpz_Pr_68_P = DynAccessor(104677)
            Pl35_CS_57_Sokol = DynAccessor(104678)

        mtl_universal = _mtl_universal()

    lootbox_reward_video = _lootbox_reward_video()

    class _personal_mission(DynAccessor):
        __slots__ = ()
        intro_video = DynAccessor(104679)
        operation_10 = DynAccessor(104680)
        operation_8 = DynAccessor(104681)
        operation_9 = DynAccessor(104682)
        operation_99 = DynAccessor(104683)
        video_operations_person = DynAccessor(104684)

    personal_mission = _personal_mission()

    class _platoon(DynAccessor):
        __slots__ = ()
        VoiceChat = DynAccessor(104685)

    platoon = _platoon()

    class _portal(DynAccessor):
        __slots__ = ()
        portal_intro = DynAccessor(104686)
        portal_outro = DynAccessor(104687)

        class _abilities(DynAccessor):
            __slots__ = ()
            berserk_portal = DynAccessor(104688)
            curse_shot_portal = DynAccessor(104689)
            fire_shot_portal = DynAccessor(104690)
            frozen_shot_portal = DynAccessor(104691)
            guided_missile_portal = DynAccessor(104692)
            laugh_shot_portal = DynAccessor(104693)
            minefield_portal = DynAccessor(104694)
            reload_aura_portal = DynAccessor(104695)
            sentry_gun_portal = DynAccessor(104696)
            shield_portal = DynAccessor(104697)
            trap_portal = DynAccessor(104698)
            vehicle_change_shot_portal = DynAccessor(104699)

        abilities = _abilities()

    portal = _portal()

    class _vehicle(DynAccessor):
        __slots__ = ()
        A122_TS_5 = DynAccessor(104700)

    vehicle = _vehicle()