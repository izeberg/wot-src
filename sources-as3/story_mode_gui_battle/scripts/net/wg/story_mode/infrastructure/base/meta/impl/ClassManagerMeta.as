package net.wg.story_mode.infrastructure.base.meta.impl
{
   import net.wg.story_mode.battle.StoryModeBattlePage;
   import net.wg.story_mode.battle.views.consumablesPanel.StoryModeConsumablesPanel;
   import net.wg.story_mode.battle.views.gameMessagesPanel.StoryModeGameMessagesPanel;
   import net.wg.story_mode.battle.views.intro.IntroVideo;
   import net.wg.story_mode.battle.views.intro.IntroVideoSubtitle;
   import net.wg.story_mode.battle.views.intro.data.IntroVideoVO;
   import net.wg.story_mode.battle.views.subtitles.StoryModeSubtitles;
   import net.wg.story_mode.battle.views.timer.StoryModeTimer;
   import net.wg.story_mode.battle.views.timer.controls.TimerGoalText;
   import net.wg.story_mode.battle.views.timer.controls.TimerMessage;
   import net.wg.story_mode.battle.views.timer.controls.TimerMovie;
   import net.wg.story_mode.battle.views.timer.controls.TimerTask;
   import net.wg.story_mode.battle.views.timer.controls.TimerTaskBar;
   import net.wg.story_mode.battle.views.timer.controls.TimerText;
   import net.wg.story_mode.data.constants.generated.STORY_MODE_BATTLE_VIEW_ALIASES;
   import net.wg.story_mode.infrastructure.base.meta.IStoryModeSubtitlesMeta;
   
   public class ClassManagerMeta
   {
      
      public static const NET_WG_STORY_MODE_BATTLE_STORYMODEBATTLEPAGE:Class = StoryModeBattlePage;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_CONSUMABLESPANEL_STORYMODECONSUMABLESPANEL:Class = StoryModeConsumablesPanel;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_GAMEMESSAGESPANEL_STORYMODEGAMEMESSAGESPANEL:Class = StoryModeGameMessagesPanel;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_INTRO_INTROVIDEO:Class = IntroVideo;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_INTRO_INTROVIDEOSUBTITLE:Class = IntroVideoSubtitle;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_INTRO_DATA_INTROVIDEOVO:Class = IntroVideoVO;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_SUBTITLES_STORYMODESUBTITLES:Class = StoryModeSubtitles;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_STORYMODETIMER:Class = StoryModeTimer;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_CONTROLS_TIMERGOALTEXT:Class = TimerGoalText;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_CONTROLS_TIMERMESSAGE:Class = TimerMessage;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_CONTROLS_TIMERMOVIE:Class = TimerMovie;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_CONTROLS_TIMERTASK:Class = TimerTask;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_CONTROLS_TIMERTASKBAR:Class = TimerTaskBar;
      
      public static const NET_WG_STORY_MODE_BATTLE_VIEWS_TIMER_CONTROLS_TIMERTEXT:Class = TimerText;
      
      public static const NET_WG_STORY_MODE_DATA_CONSTANTS_GENERATED_STORY_MODE_BATTLE_VIEW_ALIASES:Class = STORY_MODE_BATTLE_VIEW_ALIASES;
      
      public static const NET_WG_STORY_MODE_INFRASTRUCTURE_BASE_META_ISTORYMODESUBTITLESMETA:Class = IStoryModeSubtitlesMeta;
      
      public static const NET_WG_STORY_MODE_INFRASTRUCTURE_BASE_META_IMPL_STORYMODESUBTITLESMETA:Class = StoryModeSubtitlesMeta;
       
      
      public function ClassManagerMeta()
      {
         super();
      }
   }
}
