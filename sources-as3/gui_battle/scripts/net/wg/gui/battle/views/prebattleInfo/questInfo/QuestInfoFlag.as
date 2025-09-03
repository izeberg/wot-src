package net.wg.gui.battle.views.prebattleInfo.questInfo
{
   import fl.motion.easing.Quartic;
   import flash.display.BlendMode;
   import flash.display.MovieClip;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormat;
   import net.wg.data.constants.Fonts;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.prebattleInfo.PrebattleInfoViewBase;
   import net.wg.gui.components.controls.TextFieldContainer;
   import scaleform.clik.motion.Tween;
   
   public class QuestInfoFlag extends PrebattleInfoViewBase
   {
      
      private static const SHARP_CHAR:String = "#";
      
      private static const MIN_TITLE_HEIGHT:int = 50;
      
      private static const FLAG_BG_LARGE_SCALE:Number = 1;
      
      private static const FLAG_BG_SMALL_SCALE:Number = 0.75;
      
      private static const FLAG_BG_TIME:int = 500;
      
      private static const FLAG_BG_SHOW_DELAY:int = 300;
      
      private static const FLAG_BG_Y:int = -60;
      
      private static const DISABLED_QUEST_TEXT_COLOR:uint = 16777215;
      
      private static const EMPTY_SATURATION:int = 0;
      
      private static const FULL_SATURATION:int = 100;
       
      
      public var taskIndex:TextFieldContainer = null;
      
      public var taskTitle:TextFieldContainer = null;
      
      public var taskStatus:TextFieldContainer = null;
      
      public var taskIcoContainer:QuestInfoFlagTaskIcoContainer = null;
      
      public var flagBg:QuestInfoFlagBg = null;
      
      public var sparksMC:MovieClip = null;
      
      public var flashMC:MovieClip = null;
      
      private var _flagBgeTween:Tween = null;
      
      private var _textFormatLarge:TextFormat;
      
      private var _textFormatSmall:TextFormat;
      
      private var _statusTextFormatLarge:TextFormat;
      
      private var _statusTextFormatSmall:TextFormat;
      
      private var _data:QuestInfoFlagVO = null;
      
      public function QuestInfoFlag()
      {
         this._textFormatLarge = new TextFormat(Fonts.TITLE_FONT,36,16777215);
         this._textFormatSmall = new TextFormat(Fonts.TITLE_FONT,24,16777215);
         this._statusTextFormatLarge = new TextFormat(Fonts.TITLE_FONT,18,16739447);
         this._statusTextFormatSmall = new TextFormat(Fonts.TITLE_FONT,14,16739447);
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.taskIndex.noTranslateTextfield = true;
         this.taskTitle.noTranslateTextfield = true;
         this.taskTitle.isMultiline = true;
         hintContainer.noTranslateTextfield = true;
         this.taskTitle.textField.autoSize = TextFieldAutoSize.CENTER;
         this.taskStatus.autoSize = TextFieldAutoSize.CENTER;
      }
      
      override protected function doLayout(param1:Boolean) : void
      {
         super.doLayout(param1);
         this.flagBg.scaleX = this.flagBg.scaleY = !!param1 ? Number(FLAG_BG_SMALL_SCALE) : Number(FLAG_BG_LARGE_SCALE);
         this.updateTitleTextFormat(param1);
         this.updateStatusTextFormat(param1);
         this.updateTaskStatusTextPositionY(this.taskTitle.textField.height);
      }
      
      override protected function prepareData(param1:Object) : void
      {
         super.prepareData(param1);
         this._data = new QuestInfoFlagVO(param1);
      }
      
      override protected function onDispose() : void
      {
         this._data.dispose();
         this._data = null;
         this.taskIndex.dispose();
         this.taskIndex = null;
         this.taskTitle.dispose();
         this.taskTitle = null;
         this.taskIcoContainer.dispose();
         this.taskIcoContainer = null;
         this.flagBg.dispose();
         this.flagBg = null;
         this._textFormatLarge = null;
         this._textFormatSmall = null;
         if(this._flagBgeTween)
         {
            this._flagBgeTween.dispose();
            this._flagBgeTween = null;
         }
         if(this.flashMC)
         {
            this.flashMC = null;
         }
         if(this.sparksMC)
         {
            this.sparksMC = null;
         }
         this.taskStatus.dispose();
         this.taskStatus = null;
         super.onDispose();
      }
      
      override protected function updateData(param1:Boolean) : void
      {
         super.updateData(param1);
         this.taskTitle.label = this._data.questName;
         this.taskIndex.label = SHARP_CHAR + this._data.questIndexStr;
         this.taskIndex.textColor = !!this._data.isProgressAvailable ? uint(this.taskIndex.textColor) : uint(DISABLED_QUEST_TEXT_COLOR);
         this.taskIcoContainer.setData(this._data.questIcon);
         if(this._data.canBeDisabled)
         {
            this.taskIcoContainer.setTaskIconBlendMode(BlendMode.NORMAL);
            this.taskIcoContainer.setTaskIconSaturation(!!this._data.isProgressAvailable ? Number(FULL_SATURATION) : Number(EMPTY_SATURATION));
            this.flagBg.setScaledFlagBlendMode(BlendMode.NORMAL);
            this.flagBg.setScaledFlagSaturation(!!this._data.isProgressAvailable ? Number(FULL_SATURATION) : Number(EMPTY_SATURATION));
         }
         var _loc2_:int = Math.max(Values.ZERO,this.taskTitle.height - MIN_TITLE_HEIGHT);
         this.flagBg.setDeltaHeight(_loc2_);
         this.updateTitleTextFormat(param1);
         this.taskStatus.label = this._data.questStatus;
         this.taskStatus.textVisibility = !this._data.isProgressAvailable;
         this.updateStatusTextFormat(param1);
         this.updateTaskStatusTextPositionY(this.taskTitle.textField.height);
      }
      
      override protected function onAnimationTimerInit() : void
      {
         super.onAnimationTimerInit();
         this.flagBg.y = 0;
         this.flagBg.alpha = 1;
         this.flagBg.visible = true;
      }
      
      override protected function onAnimationShowInfo() : void
      {
         this.flagBg.y = FLAG_BG_Y;
         this.flagBg.alpha = 0;
         this.flagBg.visible = true;
         if(this._flagBgeTween)
         {
            this._flagBgeTween.dispose();
         }
         this._flagBgeTween = new Tween(FLAG_BG_TIME,this.flagBg,{
            "alpha":1,
            "y":0
         },{
            "delay":FLAG_BG_SHOW_DELAY,
            "ease":Quartic.easeOut,
            "paused":false
         });
         this.toggleSparkFlashAnimation(this._data.isProgressAvailable);
      }
      
      override protected function onAnimationHideInfo() : void
      {
         if(this._flagBgeTween)
         {
            this._flagBgeTween.dispose();
         }
         this._flagBgeTween = new Tween(FLAG_BG_TIME,this.flagBg,{
            "alpha":0,
            "y":FLAG_BG_Y
         },{
            "ease":Quartic.easeOut,
            "paused":false
         });
      }
      
      override protected function onAnimationInfoBgHide() : void
      {
         this.flagBg.visible = false;
      }
      
      private function updateTitleTextFormat(param1:Boolean) : void
      {
         this.taskTitle.textFormat = !!param1 ? this._textFormatSmall : this._textFormatLarge;
      }
      
      override public function get hasAnimation() : Boolean
      {
         return true;
      }
      
      private function toggleSparkFlashAnimation(param1:Boolean) : void
      {
         this.flashMC.visible = param1;
         this.sparksMC.visible = param1;
      }
      
      private function updateStatusTextFormat(param1:Boolean) : void
      {
         this.taskStatus.textFormat = !!param1 ? this._statusTextFormatSmall : this._statusTextFormatLarge;
      }
      
      private function updateTaskStatusTextPositionY(param1:Number) : void
      {
         this.taskStatus.textOffsetY = param1;
      }
   }
}
