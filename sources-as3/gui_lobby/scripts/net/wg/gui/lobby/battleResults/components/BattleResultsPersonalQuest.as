package net.wg.gui.lobby.battleResults.components
{
   import flash.display.DisplayObjectContainer;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import flash.text.TextFieldAutoSize;
   import net.wg.data.VO.BattleResultsQuestVO;
   import net.wg.data.constants.Directions;
   import net.wg.data.constants.SoundTypes;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.events.QuestEvent;
   import net.wg.gui.interfaces.ISoundButtonEx;
   import net.wg.gui.lobby.interfaces.ISubtaskComponent;
   import net.wg.gui.lobby.questsWindow.data.PersonalInfoVO;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.utils.IClassFactory;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.constants.LayoutMode;
   import scaleform.clik.events.ButtonEvent;
   
   public class BattleResultsPersonalQuest extends UIComponentEx implements ISubtaskComponent
   {
      
      private static const LINE_SEPARATOR_PADDING:int = 5;
      
      private static const LINK_BTN:String = "LinkBtn_UI";
      
      private static const CONDITIONS_BASE_OFFSET:int = 19;
      
      private static const LINK_BTN_PADDING_TOP:int = 1;
      
      private static const LINK_BTN_PADDING_LEFT:int = 8;
      
      private static const LINK_BTN_PADDING_H:int = 5;
      
      private static const BOTTOM_QUEST_OFFSET:int = 24;
      
      private static const QUEST_STATUS_PADDING_TOP:int = 4;
      
      private static const QUEST_DESCR_CONTENT_TF_Y:int = 38;
      
      private static const QUEST_DESCR_TF_Y:int = 29;
      
      private static const TF_X:int = 20;
      
      private static const TF_HAS_CONTENT_X:int = 38;
      
      private static const STATE_RIGHT:int = 16;
      
      private static const DOTS:String = "...";
      
      private static const QUEST_TITLE_TF_MAX_WIDTH:int = 280;
      
      private static const PERSONAL_QUEST_LINK:String = "PersonalConditionUI";
       
      
      public var questTitleTF:TextField = null;
      
      public var questDescrTF:TextField = null;
      
      public var questStatus:PersonalQuestState = null;
      
      public var lineMC:MovieClip = null;
      
      public var collapsedToggleBtn:ISoundButtonEx = null;
      
      public var quests:Vector.<PersonalCondition> = null;
      
      private var _model:BattleResultsQuestVO = null;
      
      private var _linkBtn:SoundButtonEx = null;
      
      private var _hasQuestDescr:Boolean = false;
      
      private var _factory:IClassFactory;
      
      private var _toolTipMgr:ITooltipMgr;
      
      private var prevCondHeight:int = 0;
      
      private var lastYpos:int = 0;
      
      public function BattleResultsPersonalQuest()
      {
         this._factory = App.utils.classFactory;
         this._toolTipMgr = App.toolTipMgr;
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.collapsedToggleBtn.selected = true;
         this.collapsedToggleBtn.addEventListener(ButtonEvent.CLICK,this.onCollapsedToggleBtnClickHandler);
         this.quests = new Vector.<PersonalCondition>();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(this._model != null && isInvalid(InvalidationType.DATA))
         {
            this.questTitleTF.autoSize = TextFieldAutoSize.LEFT;
            this.questTitleTF.htmlText = this._model.title;
            if(this.questTitleTF.width > QUEST_TITLE_TF_MAX_WIDTH)
            {
               this.questTitleTF.autoSize = TextFieldAutoSize.NONE;
               this.questTitleTF.width = QUEST_TITLE_TF_MAX_WIDTH;
               App.utils.commons.truncateTextFieldText(this.questTitleTF,this._model.title,true,true,DOTS);
               this.questTitleTF.addEventListener(MouseEvent.ROLL_OUT,this.onQuestTitleTFRollOutHandler);
               this.questTitleTF.addEventListener(MouseEvent.ROLL_OVER,this.onQuestTitleTFRollOverHandler);
               App.utils.commons.updateTextFieldSize(this.questTitleTF,true,false);
            }
            this.questTitleTF.x = !!this._model.collapsedToggleBtnVisible ? Number(TF_HAS_CONTENT_X) : Number(TF_X);
            this.questStatus.update(this._model.questState);
            if(this._model.linkBtnVisible && this._linkBtn == null)
            {
               this.createLinkBtn();
            }
            if(this._linkBtn != null)
            {
               this._linkBtn.visible = this._model.linkBtnVisible;
            }
            this.collapsedToggleBtn.visible = this._model.collapsedToggleBtnVisible;
            this._hasQuestDescr = StringUtils.isNotEmpty(this._model.descr);
            this.questDescrTF.visible = this._hasQuestDescr;
            if(this._hasQuestDescr)
            {
               this.questDescrTF.x = this.questTitleTF.x;
               this.questDescrTF.htmlText = this._model.descr;
               App.utils.commons.updateTextFieldSize(this.questDescrTF);
            }
            this.deleteConditions();
            this.setQuestInfo();
            this.doLayout();
         }
      }
      
      private function setQuestInfo() : void
      {
         var _loc3_:Boolean = false;
         var _loc4_:int = 0;
         var _loc5_:PersonalInfoVO = null;
         var _loc6_:PersonalCondition = null;
         var _loc1_:int = this._model.personalInfo.length;
         var _loc2_:int = 0;
         while(_loc2_ < _loc1_)
         {
            _loc3_ = _loc2_ % 2 == 0;
            _loc4_ = 0;
            while(_loc4_ < this._model.personalInfo[_loc2_].length)
            {
               _loc5_ = this._model.personalInfo[_loc2_][_loc4_];
               _loc6_ = this.createCondition(_loc5_.text,_loc5_.statusText,_loc3_);
               this.quests.push(_loc6_);
               _loc4_++;
            }
            _loc2_++;
         }
         this.setQuestPosition();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:PersonalCondition = null;
         if(this._linkBtn != null)
         {
            this._linkBtn.removeEventListener(ButtonEvent.CLICK,this.onLinkBtnClickHandler);
            this._linkBtn.removeEventListener(MouseEvent.ROLL_OUT,this.onLinkBtnRollOutHandler);
            this._linkBtn.removeEventListener(MouseEvent.ROLL_OVER,this.onLinkBtnRollOverHandler);
            this._linkBtn.dispose();
            removeChild(this._linkBtn);
            this._linkBtn = null;
         }
         if(this._model != null)
         {
            this._model.dispose();
            this._model = null;
         }
         if(this.lineMC != null)
         {
            removeChild(this.lineMC);
            this.lineMC = null;
         }
         this.questStatus.dispose();
         this.questStatus = null;
         this.collapsedToggleBtn.removeEventListener(ButtonEvent.CLICK,this.onCollapsedToggleBtnClickHandler);
         this.collapsedToggleBtn.dispose();
         this.collapsedToggleBtn = null;
         this.questTitleTF.removeEventListener(MouseEvent.ROLL_OUT,this.onQuestTitleTFRollOutHandler);
         this.questTitleTF.removeEventListener(MouseEvent.ROLL_OVER,this.onQuestTitleTFRollOverHandler);
         this.questTitleTF = null;
         this._factory = null;
         this._toolTipMgr = null;
         this.deleteConditions();
         for each(_loc1_ in this.quests)
         {
            _loc1_.dispose();
         }
         this.quests.splice(0,this.quests.length);
         this.quests = null;
         super.onDispose();
      }
      
      public function disableLinkBtns(param1:Vector.<String>) : void
      {
         this._linkBtn.enabled = param1.indexOf(this._model.questInfo.questID) != -1;
         this._linkBtn.mouseEnabled = true;
      }
      
      public function setData(param1:Object) : void
      {
         this._model = new BattleResultsQuestVO(param1);
         invalidateData();
      }
      
      private function makeComponent(param1:String) : DisplayObjectContainer
      {
         return this._factory.getComponent(param1,DisplayObjectContainer);
      }
      
      private function doLayout() : void
      {
         var _loc1_:int = 0;
         var _loc2_:int = 0;
         this.questStatus.x = width - this.questStatus.width - STATE_RIGHT | 0;
         this.questStatus.y = this.questTitleTF.y + QUEST_STATUS_PADDING_TOP | 0;
         this.lineMC.y = this.questTitleTF.y + this.questTitleTF.height + LINE_SEPARATOR_PADDING | 0;
         if(this._linkBtn != null)
         {
            this._linkBtn.x = this.questTitleTF.x + this.questTitleTF.width + LINK_BTN_PADDING_LEFT | 0;
            this._linkBtn.y = this.questTitleTF.y + (this.questTitleTF.height - this._linkBtn.height >> 1) + LINK_BTN_PADDING_TOP | 0;
         }
         if(this.collapsedToggleBtn.selected && this._model.collapsedToggleBtnVisible && this._model.personalInfo != null)
         {
            this.questDescrTF.y = QUEST_DESCR_CONTENT_TF_Y;
            this.setQuestPosition();
            this.lineMC.y = this.lastYpos + this.prevCondHeight + LINE_SEPARATOR_PADDING | 0;
            this.questDescrTF.visible = this._hasQuestDescr;
            _loc1_ = 0;
            while(_loc1_ < this.quests.length)
            {
               this.quests[_loc1_].visible = true;
               _loc1_++;
            }
         }
         else
         {
            if(this._hasQuestDescr && !this._model.collapsedToggleBtnVisible)
            {
               this.questDescrTF.y = QUEST_DESCR_TF_Y;
               this.questDescrTF.visible = true;
               this.lineMC.y = this.questDescrTF.y + this.questDescrTF.height + LINE_SEPARATOR_PADDING | 0;
            }
            else
            {
               this.questDescrTF.y = 0;
               this.questDescrTF.visible = false;
            }
            _loc2_ = 0;
            while(_loc2_ < this.quests.length)
            {
               this.quests[_loc2_].y = 0;
               this.quests[_loc2_].visible = false;
               _loc2_++;
            }
         }
         setSize(width,this.lineMC.y);
         dispatchEvent(new Event(Event.RESIZE,true));
      }
      
      private function setQuestPosition() : void
      {
         var _loc1_:PersonalCondition = null;
         this.prevCondHeight = 0;
         this.lastYpos = 0;
         for each(_loc1_ in this.quests)
         {
            if(this.lastYpos <= 0)
            {
               this.lastYpos = CONDITIONS_BASE_OFFSET;
            }
            else
            {
               this.lastYpos = CONDITIONS_BASE_OFFSET / 2 - 2 + this.prevCondHeight;
            }
            _loc1_.y = this.lastYpos;
            this.prevCondHeight = _loc1_.getTextHeight() + BOTTOM_QUEST_OFFSET;
         }
      }
      
      private function createCondition(param1:String, param2:String, param3:Boolean) : PersonalCondition
      {
         var _loc4_:PersonalCondition = App.utils.classFactory.getComponent(PERSONAL_QUEST_LINK,PersonalCondition);
         _loc4_.setData(param1,param2,param3);
         var _loc5_:Function = !!param3 ? this.onMainConditionTFRollOverHandler : this.onAdditionalConditionTFRollOverHandler;
         var _loc6_:Function = !!param3 ? this.onMainConditionTFRollOutHandler : this.onAdditionalConditionTFRollOutHandler;
         _loc4_.addEventListener(MouseEvent.ROLL_OVER,_loc5_);
         _loc4_.addEventListener(MouseEvent.ROLL_OUT,_loc6_);
         addChild(_loc4_);
         return _loc4_;
      }
      
      private function deleteConditions() : void
      {
         var _loc1_:PersonalCondition = null;
         var _loc2_:Function = null;
         var _loc3_:Function = null;
         if(this.quests != null)
         {
            for each(_loc1_ in this.quests)
            {
               removeChild(_loc1_);
               _loc2_ = !!_loc1_.isMainQuest() ? this.onMainConditionTFRollOverHandler : this.onAdditionalConditionTFRollOverHandler;
               _loc3_ = !!_loc1_.isMainQuest() ? this.onMainConditionTFRollOutHandler : this.onAdditionalConditionTFRollOutHandler;
               _loc1_.removeEventListener(MouseEvent.ROLL_OVER,_loc2_);
               _loc1_.removeEventListener(MouseEvent.ROLL_OUT,_loc3_);
               _loc1_.dispose();
            }
            this.quests.splice(0,this.quests.length);
         }
      }
      
      private function createLinkBtn() : void
      {
         this._linkBtn = SoundButtonEx(this.makeComponent(LINK_BTN));
         this._linkBtn.autoSize = LayoutMode.ALIGN_NONE;
         this._linkBtn.helpDirection = Directions.TOP;
         this._linkBtn.paddingHorizontal = LINK_BTN_PADDING_H;
         this._linkBtn.soundType = SoundTypes.NORMAL_BTN;
         this._linkBtn.scaleX = this._linkBtn.scaleY = 1;
         addChild(this._linkBtn);
         this._linkBtn.addEventListener(ButtonEvent.CLICK,this.onLinkBtnClickHandler);
         this._linkBtn.addEventListener(MouseEvent.ROLL_OUT,this.onLinkBtnRollOutHandler);
         this._linkBtn.addEventListener(MouseEvent.ROLL_OVER,this.onLinkBtnRollOverHandler);
      }
      
      private function onMainConditionTFRollOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.show(TOOLTIPS.QUESTS_PM_STATUS_MAIN);
      }
      
      private function onMainConditionTFRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onAdditionalConditionTFRollOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.show(TOOLTIPS.QUESTS_PM_STATUS_ADDITIONAL);
      }
      
      private function onAdditionalConditionTFRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onLinkBtnRollOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.show(!!this._linkBtn.enabled ? this._model.questInfo.linkTooltip : TOOLTIPS.QUESTS_DISABLELINKBTN_TASK);
      }
      
      private function onLinkBtnRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onQuestTitleTFRollOverHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.show(this._model.title);
      }
      
      private function onQuestTitleTFRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onLinkBtnClickHandler(param1:ButtonEvent) : void
      {
         this._toolTipMgr.hide();
         var _loc2_:QuestEvent = new QuestEvent(QuestEvent.SELECT_QUEST,this._model.questInfo.questID);
         _loc2_.eventType = this._model.questInfo.eventType;
         dispatchEvent(_loc2_);
      }
      
      private function onCollapsedToggleBtnClickHandler(param1:ButtonEvent) : void
      {
         this.collapsedToggleBtn.selected = !this.collapsedToggleBtn.selected;
         this.doLayout();
      }
   }
}
