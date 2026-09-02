package net.wg.gui.lobby.hangar.quests
{
   import net.wg.gui.events.LobbyEvent;
   import net.wg.infrastructure.managers.IStageSizeManager;
   import net.wg.utils.IStageSizeDependComponent;
   import org.idmedia.as3commons.util.StringUtils;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.clik.motion.Tween;
   
   public class WhiteTigerWidget extends HangarWidgetInject implements IStageSizeDependComponent
   {
      
      private static const EXTRA_SMALL:String = "Extra Small";
      
      private static const SMALL:String = "Small";
      
      private static const MEDIUM:String = "Medium";
      
      private static const LARGE:String = "Large";
      
      private static const EXTRA_LARGE:String = "Extra Large";
      
      private static const SIZES:Object = {};
      
      private static const MARGIN:int = 2;
      
      private static const SIZE_SMALL:uint = 164;
      
      private static const SIZE_LARGE:uint = 188;
      
      private static const SIZE_EXTRA_LARGE:uint = 244;
      
      private static const TWEEN_FADE_DURATION:uint = 200;
      
      {
         SIZES[EXTRA_SMALL] = SIZE_SMALL + MARGIN;
         SIZES[SMALL] = SIZE_SMALL + MARGIN;
         SIZES[MEDIUM] = SIZE_LARGE + MARGIN;
         SIZES[LARGE] = SIZE_LARGE + MARGIN;
         SIZES[EXTRA_LARGE] = SIZE_EXTRA_LARGE + MARGIN;
      }
      
      private var _tweenFade:Tween = null;
      
      private var _stageSizeMgr:IStageSizeManager;
      
      private var _currentBreakPoint:String = null;
      
      public function WhiteTigerWidget()
      {
         this._stageSizeMgr = App.stageSizeMgr;
         super();
         setManageSize(true);
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         buttonMode = useHandCursor = true;
         App.stage.addEventListener(LobbyEvent.DRAGGING_START,this.onDraggingStartHandler);
         App.stage.addEventListener(LobbyEvent.DRAGGING_END,this.onDraggingEndHandler);
         this._stageSizeMgr.register(this);
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(StringUtils.isNotEmpty(this._currentBreakPoint) && isInvalid(InvalidationType.SIZE))
         {
            width = SIZES[this._currentBreakPoint];
            height = SIZES[this._currentBreakPoint];
            x = -(width >> 1);
         }
      }
      
      override protected function onDispose() : void
      {
         this.clearTweenFade();
         App.stage.removeEventListener(LobbyEvent.DRAGGING_START,this.onDraggingStartHandler);
         App.stage.removeEventListener(LobbyEvent.DRAGGING_END,this.onDraggingEndHandler);
         this._stageSizeMgr.unregister(this);
         this._stageSizeMgr = null;
         super.onDispose();
      }
      
      public function setStateSizeBoundaries(param1:int, param2:int) : void
      {
         var _loc3_:String = this._stageSizeMgr.currentBreakPoint.name;
         if(this._currentBreakPoint != _loc3_)
         {
            this._currentBreakPoint = _loc3_;
            invalidateSize();
         }
      }
      
      private function clearTweenFade() : void
      {
         if(this._tweenFade)
         {
            this._tweenFade.dispose();
            this._tweenFade = null;
         }
      }
      
      private function onDraggingStartHandler(param1:LobbyEvent) : void
      {
         this.clearTweenFade();
         mouseChildren = false;
         this._tweenFade = new Tween(TWEEN_FADE_DURATION,this,{"alpha":0});
      }
      
      private function onDraggingEndHandler(param1:LobbyEvent) : void
      {
         this.clearTweenFade();
         mouseChildren = true;
         this._tweenFade = new Tween(TWEEN_FADE_DURATION,this,{"alpha":1});
      }
   }
}
