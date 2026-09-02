package net.wg.gui.lobby.whiteTiger
{
   import net.wg.gui.events.LobbyEvent;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.utils.StageSizeBoundaries;
   import scaleform.clik.motion.Tween;
   
   public class WtHangarComponentsContainer extends SimpleDisposable
   {
      
      private static const MARGIN:int = 2;
      
      private static const CREW_WIDGET_WIDTH:int = 469;
      
      private static const CREW_WIDGET_HEIGHT:int = 260;
      
      private static const CREW_WIDGET_WIDTH_SMALL:int = 369;
      
      private static const CREW_WIDGET_HEIGHT_SMALL:int = 212;
      
      private static const CREW_WIDGET_Y:int = 31;
      
      private static const VEH_PARAMS_WIDGET_WIDTH:int = 347;
      
      private static const VEH_PARAMS_WIDGET_HEIGHT:int = 530;
      
      private static const VEH_PARAMS_WIDGET_WIDTH_SMALL:int = 282;
      
      private static const VEH_PARAMS_WIDGET_HEIGHT_SMALL:int = 484;
      
      private static const EXTRA_SMALL:String = "Extra Small";
      
      private static const SMALL:String = "Small";
      
      private static const MEDIUM:String = "Medium";
      
      private static const LARGE:String = "Large";
      
      private static const EXTRA_LARGE:String = "Extra Large";
      
      private static const CAROUSEL_WIDGET_WIDTH:Object = {};
      
      private static const CAROUSEL_WIDGET_HEIGHT:Object = {};
      
      private static const LOOT_BOXES_WIDGET_SIZE:Object = {};
      
      private static const TWEEN_FADE_DURATION:uint = 200;
      
      {
         CAROUSEL_WIDGET_WIDTH[EXTRA_SMALL] = 1024;
         CAROUSEL_WIDGET_WIDTH[SMALL] = 1044;
         CAROUSEL_WIDGET_WIDTH[MEDIUM] = 1124;
         CAROUSEL_WIDGET_WIDTH[LARGE] = 1475;
         CAROUSEL_WIDGET_WIDTH[EXTRA_LARGE] = 1670;
         CAROUSEL_WIDGET_HEIGHT[EXTRA_SMALL] = 266;
         CAROUSEL_WIDGET_HEIGHT[SMALL] = 266;
         CAROUSEL_WIDGET_HEIGHT[MEDIUM] = 266;
         CAROUSEL_WIDGET_HEIGHT[LARGE] = 360;
         CAROUSEL_WIDGET_HEIGHT[EXTRA_LARGE] = 360;
         LOOT_BOXES_WIDGET_SIZE[EXTRA_SMALL] = [152 + MARGIN,120 + MARGIN];
         LOOT_BOXES_WIDGET_SIZE[SMALL] = [152 + MARGIN,120 + MARGIN];
         LOOT_BOXES_WIDGET_SIZE[MEDIUM] = [240 + MARGIN,180 + MARGIN];
         LOOT_BOXES_WIDGET_SIZE[LARGE] = [240 + MARGIN,180 + MARGIN];
         LOOT_BOXES_WIDGET_SIZE[EXTRA_LARGE] = [276 + MARGIN,212 + MARGIN];
      }
      
      public var lootBoxesWidget:WtHangarBaseWidget = null;
      
      public var carouselWidget:WtHangarBaseWidget = null;
      
      public var crewWidget:WtHangarBaseWidget = null;
      
      public var vehicleParamsWidget:WtHangarBaseWidget = null;
      
      private var _lootBoxesVisible:Boolean = true;
      
      private var _tweenFade:Tween = null;
      
      public function WtHangarComponentsContainer()
      {
         super();
         this.carouselWidget = new WtHangarBaseWidget();
         this.carouselWidget.name = "wtCarouselWidget";
         addChild(this.carouselWidget);
         this.crewWidget = new WtHangarBaseWidget();
         this.crewWidget.name = "wtCrewWidget";
         addChild(this.crewWidget);
         this.crewWidget.y = CREW_WIDGET_Y;
         this.vehicleParamsWidget = new WtHangarBaseWidget();
         this.vehicleParamsWidget.name = "wtVehicleParamsWidget";
         addChild(this.vehicleParamsWidget);
         this.vehicleParamsWidget.y = CREW_WIDGET_Y;
         this.lootBoxesWidget = new WtHangarBaseWidget();
         this.lootBoxesWidget.name = "wtLootBoxesWidget";
         addChild(this.lootBoxesWidget);
         App.stage.addEventListener(LobbyEvent.DRAGGING_START,this.onDraggingStartHandler);
         App.stage.addEventListener(LobbyEvent.DRAGGING_END,this.onDraggingEndHandler);
      }
      
      override protected function onDispose() : void
      {
         this.clearTweenFade();
         App.stage.removeEventListener(LobbyEvent.DRAGGING_START,this.onDraggingStartHandler);
         App.stage.removeEventListener(LobbyEvent.DRAGGING_END,this.onDraggingEndHandler);
         this.carouselWidget = null;
         this.crewWidget = null;
         this.vehicleParamsWidget = null;
         this.lootBoxesWidget = null;
      }
      
      public function setLootBoxesVisible(param1:Boolean) : void
      {
         if(param1 != this._lootBoxesVisible)
         {
            this._lootBoxesVisible = param1;
            if(this.lootBoxesWidget)
            {
               this.lootBoxesWidget.visible = this._lootBoxesVisible;
            }
         }
      }
      
      public function updateStage(param1:int, param2:int) : void
      {
         var _loc5_:int = 0;
         var _loc6_:int = 0;
         var _loc7_:int = 0;
         var _loc8_:int = 0;
         var _loc3_:Boolean = App.appHeight < StageSizeBoundaries.HEIGHT_900 || App.appWidth < StageSizeBoundaries.WIDTH_1600;
         var _loc4_:String = App.stageSizeMgr.currentBreakPoint.name;
         if(this.crewWidget)
         {
            this.crewWidget.setSize(!!_loc3_ ? Number(CREW_WIDGET_WIDTH_SMALL) : Number(CREW_WIDGET_WIDTH),!!_loc3_ ? Number(CREW_WIDGET_HEIGHT_SMALL) : Number(CREW_WIDGET_HEIGHT));
         }
         if(this.vehicleParamsWidget)
         {
            this.vehicleParamsWidget.setSize(!!_loc3_ ? Number(VEH_PARAMS_WIDGET_WIDTH_SMALL) : Number(VEH_PARAMS_WIDGET_WIDTH),!!_loc3_ ? Number(VEH_PARAMS_WIDGET_HEIGHT_SMALL) : Number(VEH_PARAMS_WIDGET_HEIGHT));
            this.vehicleParamsWidget.x = param1 - this.vehicleParamsWidget.width;
         }
         if(this.carouselWidget)
         {
            _loc5_ = CAROUSEL_WIDGET_WIDTH[_loc4_];
            _loc6_ = CAROUSEL_WIDGET_HEIGHT[_loc4_];
            this.carouselWidget.setSize(_loc5_,_loc6_);
            this.carouselWidget.x = param1 > _loc5_ ? Number(param1 - _loc5_ >> 1) : Number(0);
            this.carouselWidget.y = param2 - _loc6_;
         }
         if(this.lootBoxesWidget)
         {
            _loc7_ = LOOT_BOXES_WIDGET_SIZE[_loc4_][0];
            _loc8_ = LOOT_BOXES_WIDGET_SIZE[_loc4_][1];
            this.lootBoxesWidget.setSize(_loc7_,_loc8_);
            this.lootBoxesWidget.x = param1 - _loc7_;
            this.lootBoxesWidget.y = param2 - _loc8_;
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
