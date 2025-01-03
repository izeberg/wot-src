package net.wg.gui.lobby.hangar
{
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.text.TextFieldAutoSize;
   import flash.text.TextFormatAlign;
   import net.wg.data.constants.Linkages;
   import net.wg.data.constants.UniversalBtnStylesConst;
   import net.wg.data.constants.generated.TOOLTIPS_CONSTANTS;
   import net.wg.gui.components.common.Counter;
   import net.wg.gui.components.controls.Image;
   import net.wg.gui.components.controls.universalBtn.UniversalBtn;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import net.wg.infrastructure.managers.ITooltipMgr;
   import net.wg.infrastructure.managers.counter.CounterManager;
   import net.wg.infrastructure.managers.counter.CounterProps;
   import net.wg.utils.ICounterManager;
   
   public class VehPostProgressionBtn extends Sprite implements IDisposable
   {
      
      private static const ICON_LOCK_Y:int = 4;
      
      private static const ENTRY_POINT_PARENT_SCREEN:String = "hangar";
       
      
      public var button:UniversalBtn = null;
      
      private var _iconLock:Image = null;
      
      private var _intCD:int = -1;
      
      private var _tooltipManager:ITooltipMgr = null;
      
      private var _counterManager:ICounterManager = null;
      
      private var _disposed:Boolean = false;
      
      public function VehPostProgressionBtn()
      {
         super();
         this._tooltipManager = App.toolTipMgr;
         this._counterManager = App.utils.counterManager;
         this._iconLock = new Image();
         this._iconLock.mouseEnabled = false;
         this._iconLock.visible = false;
         this._iconLock.addEventListener(Event.CHANGE,this.onIconLockChangeHandler);
         this._iconLock.source = RES_ICONS.MAPS_ICONS_BUTTONS_PP_LOCK;
         addChild(this._iconLock);
         App.utils.universalBtnStyles.setStyle(this.button,UniversalBtnStylesConst.STYLE_SLIM_GREEN);
         this.button.focusable = false;
         this.button.iconAlign = TextFieldAutoSize.CENTER;
         this.button.iconSource = RES_ICONS.MAPS_ICONS_BUTTONS_PP_ICON;
         this.button.addEventListener(Event.RESIZE,this.onButtonResize);
         addEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         addEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         addEventListener(MouseEvent.MOUSE_DOWN,this.onMouseDownHandler);
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.onDispose();
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      protected function onDispose() : void
      {
         this.button.removeEventListener(Event.RESIZE,this.onButtonResize);
         removeEventListener(MouseEvent.ROLL_OVER,this.onRollOverHandler);
         removeEventListener(MouseEvent.ROLL_OUT,this.onRollOutHandler);
         removeEventListener(MouseEvent.MOUSE_DOWN,this.onMouseDownHandler);
         this._iconLock.removeEventListener(Event.CHANGE,this.onIconLockChangeHandler);
         this._iconLock.dispose();
         this._iconLock = null;
         this._tooltipManager = null;
         this._counterManager.removeCounter(this);
         this._counterManager = null;
      }
      
      public function set enabled(param1:Boolean) : void
      {
         this.button.enabled = param1;
         this._iconLock.visible = !param1;
      }
      
      public function set intCD(param1:int) : void
      {
         this._intCD = param1;
      }
      
      public function set showCounter(param1:Boolean) : void
      {
         var _loc2_:CounterProps = null;
         if(param1)
         {
            _loc2_ = new CounterProps(3,2,TextFormatAlign.LEFT,true,Linkages.COUNTER_UI,CounterProps.DEFAULT_TF_PADDING,false,Counter.EMPTY_STATE);
            this._counterManager.setCounter(this,CounterManager.COUNTER_EMPTY,null,_loc2_);
         }
         else
         {
            this._counterManager.removeCounter(this);
         }
      }
      
      private function onRollOverHandler(param1:MouseEvent) : void
      {
         this._tooltipManager.showWulfTooltip(TOOLTIPS_CONSTANTS.VEH_POST_PROGRESSION_ENTRY_POINT,this._intCD,ENTRY_POINT_PARENT_SCREEN);
      }
      
      private function onRollOutHandler(param1:MouseEvent) : void
      {
         this._tooltipManager.hide();
      }
      
      private function onMouseDownHandler(param1:MouseEvent) : void
      {
         this._tooltipManager.hide();
      }
      
      private function onIconLockChangeHandler(param1:Event) : void
      {
         this._iconLock.x = width - this._iconLock.width >> 1;
         this._iconLock.y = ICON_LOCK_Y;
         dispatchEvent(new Event(Event.RESIZE));
      }
      
      private function onButtonResize(param1:Event) : void
      {
         dispatchEvent(new Event(Event.RESIZE));
      }
   }
}
