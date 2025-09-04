package net.wg.gui.lobby.userMissions.components
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.wg.data.constants.SoundManagerStates;
   import net.wg.data.constants.SoundTypes;
   import net.wg.data.constants.generated.QUESTS_ALIASES;
   import net.wg.gui.components.carousels.interfaces.IFilterCounter;
   import net.wg.gui.components.controls.IconTextButton;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.interfaces.IPopOverCaller;
   import net.wg.infrastructure.managers.IPopoverManager;
   import net.wg.infrastructure.managers.ISoundManager;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.events.ButtonEvent;
   
   public class MissionsFilter extends UIComponentEx implements IPopOverCaller
   {
      
      private static const FILTER_BUTTON_ICON_OFFSET_LEFT:int = 10;
      
      private static const FILTER_BUTTON_ICON_OFFSET_TOP:int = 1;
      
      private static const FILTER_COUNTER_Y_SHIFT:int = -41;
       
      
      public var filterIcon:Sprite;
      
      public var filterButton:IconTextButton;
      
      public var tasksLabel:TextField;
      
      public var filterCounter:IFilterCounter;
      
      private var _popoverMgr:IPopoverManager = null;
      
      private var _toolTipMgr:ITooltipMgr = null;
      
      private var _soundMgr:ISoundManager = null;
      
      public function MissionsFilter()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this._popoverMgr = App.popoverMgr;
         this._toolTipMgr = App.toolTipMgr;
         this._soundMgr = App.soundMgr;
         if(this.filterButton)
         {
            this.filterButton.addEventListener(ButtonEvent.CLICK,this.onFilterButtonClickHandler);
            this.filterButton.tooltip = QUESTS.MISSIONS_FILTER_FILTERBUTTON;
            this.filterButton.iconOffsetLeft = FILTER_BUTTON_ICON_OFFSET_LEFT;
            this.filterButton.iconOffsetTop = FILTER_BUTTON_ICON_OFFSET_TOP;
            this.filterButton.iconSource = RES_ICONS.MAPS_ICONS_BUTTONS_FILTER;
         }
         else if(this.filterIcon)
         {
            this.filterIcon.buttonMode = true;
            this.filterIcon.addEventListener(MouseEvent.ROLL_OVER,this.onMouseRollOverHandler);
            this.filterIcon.addEventListener(MouseEvent.ROLL_OUT,this.onMouseRollOutHandler);
            this.filterIcon.addEventListener(MouseEvent.MOUSE_DOWN,this.onMouseDownHandler);
            this.filterIcon.addEventListener(MouseEvent.CLICK,this.onFilterButtonClickHandler);
         }
         this.filterCounter.setCloseButtonTooltip(QUESTS.MISSIONS_FILTERCOUNTER_CLOSEBUTTON);
         this.tasksLabel.htmlText = QUESTS.MISSIONS_FILTERCOUNTER_LABEL;
         App.utils.commons.updateTextFieldSize(this.tasksLabel,true,false);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.SIZE))
         {
            this.filterCounter.x = this.tasksLabel.x + this.tasksLabel.width + FILTER_COUNTER_Y_SHIFT;
         }
      }
      
      override protected function onDispose() : void
      {
         if(this.filterButton)
         {
            this.filterButton.removeEventListener(ButtonEvent.CLICK,this.onFilterButtonClickHandler);
            this.filterButton.dispose();
            this.filterButton = null;
         }
         if(this.filterIcon)
         {
            this.filterIcon.removeEventListener(MouseEvent.CLICK,this.onFilterButtonClickHandler);
            this.filterIcon.removeEventListener(MouseEvent.ROLL_OVER,this.onMouseRollOverHandler);
            this.filterIcon.removeEventListener(MouseEvent.ROLL_OUT,this.onMouseRollOutHandler);
            this.filterIcon.removeEventListener(MouseEvent.MOUSE_DOWN,this.onMouseDownHandler);
            this.filterIcon = null;
         }
         this.filterCounter.dispose();
         this.filterCounter = null;
         this.tasksLabel = null;
         this._popoverMgr = null;
         this._toolTipMgr = null;
         this._soundMgr = null;
         super.onDispose();
      }
      
      public function blink() : void
      {
         this.filterCounter.blink();
      }
      
      public function getHitArea() : DisplayObject
      {
         return Boolean(this.filterButton) ? this.filterButton : this.filterIcon;
      }
      
      public function getTargetButton() : DisplayObject
      {
         return Boolean(this.filterButton) ? this.filterButton : this.filterIcon;
      }
      
      public function showFilterCounter(param1:String, param2:Boolean) : void
      {
         this.filterCounter.setCount(param1,false,param2);
      }
      
      private function onFilterButtonClickHandler(param1:Event) : void
      {
         this._soundMgr.playControlsSnd(SoundManagerStates.SND_PRESS,SoundTypes.NORMAL_BTN,null);
         this._popoverMgr.show(this,QUESTS_ALIASES.MISSIONS_FILTER_POPOVER_ALIAS);
      }
      
      private function onMouseDownHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
      
      private function onMouseRollOverHandler(param1:MouseEvent) : void
      {
         this._soundMgr.playControlsSnd(SoundManagerStates.SND_OVER,SoundTypes.NORMAL_BTN,null);
         this._toolTipMgr.showComplex(QUESTS.MISSIONS_FILTER_FILTERBUTTON);
      }
      
      private function onMouseRollOutHandler(param1:MouseEvent) : void
      {
         this._toolTipMgr.hide();
      }
   }
}
