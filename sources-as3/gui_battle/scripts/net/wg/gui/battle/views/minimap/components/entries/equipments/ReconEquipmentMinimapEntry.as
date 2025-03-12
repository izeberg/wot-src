package net.wg.gui.battle.views.minimap.components.entries.equipments
{
   import flash.display.MovieClip;
   import flash.events.TimerEvent;
   import flash.geom.ColorTransform;
   import flash.utils.Timer;
   import net.wg.data.constants.InvalidationType;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.battle.views.minimap.MinimapEntryController;
   import net.wg.infrastructure.events.ColorSchemeEvent;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   import scaleform.gfx.Extensions;
   
   public class ReconEquipmentMinimapEntry extends BattleUIComponent
   {
      
      private static const ALLY_COLOR:uint = 8634923;
      
      private static const ENEMY_COLOR:uint = 14098707;
      
      private static const COLORBLIND_COLOR:uint = 7959001;
      
      private static const TIMER_REPEAT:uint = 4;
      
      private static const FULL_ALPHA:Number = 1;
      
      private static const FIRST_ALPHA:Number = 1;
      
      private static const SECOND_ALPHA:Number = 1;
      
      private static const THIRD_ALPHA:Number = 0.66;
      
      private static const LAST_ALPHA:Number = 0.33;
      
      private static const TIMER_MULTIPLIER:uint = 1000;
       
      
      public var icon:MovieClip = null;
      
      public var area:MovieClip = null;
      
      public var marker:MovieClip = null;
      
      protected var colorblindMode:Boolean = false;
      
      private var _iconTimer:Timer;
      
      private var _areaTimer:Timer;
      
      private var _areaTimerDelay:Number;
      
      private var _isAlly:Boolean = false;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      private var _timerCounter:uint = 0;
      
      private var _areaSize:Number = 1;
      
      public function ReconEquipmentMinimapEntry()
      {
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
         MinimapEntryController.instance.registerScalableEntry(this);
         Extensions.setEdgeAAMode(this.icon,Extensions.EDGEAA_ON);
         Extensions.setEdgeAAMode(this.area,Extensions.EDGEAA_ON);
         Extensions.setEdgeAAMode(this.marker,Extensions.EDGEAA_ON);
      }
      
      public function setInitialData(param1:int, param2:int, param3:int, param4:Number) : void
      {
         this._isAlly = param1 > 0;
         this._areaTimerDelay = param2 * TIMER_MULTIPLIER / TIMER_REPEAT;
         this._areaSize = param4;
         this._iconTimer = new Timer(param3 * TIMER_MULTIPLIER,1);
         this._iconTimer.start();
         this._iconTimer.addEventListener(TimerEvent.TIMER_COMPLETE,this.onIconTimerComplete);
         this.marker.scaleX *= param4;
         this.marker.scaleY *= param4;
         invalidateState();
      }
      
      protected function onIconTimerComplete(param1:TimerEvent) : void
      {
         this._iconTimer.stop();
         this._iconTimer.removeEventListener(TimerEvent.TIMER_COMPLETE,this.onIconTimerComplete);
         this._areaTimer = new Timer(this._areaTimerDelay,TIMER_REPEAT);
         this._areaTimer.start();
         this._areaTimer.addEventListener(TimerEvent.TIMER,this.onAreaTimer);
         invalidateState();
      }
      
      protected function onAreaTimer(param1:TimerEvent) : void
      {
         ++this._timerCounter;
         this.setColor();
         invalidateState();
      }
      
      override protected function onDispose() : void
      {
         this._colorSchemeMgr.removeEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onSchemasUpdatedHandler);
         MinimapEntryController.instance.unregisterScalableEntry(this);
         this._areaTimer.removeEventListener(TimerEvent.TIMER,this.onAreaTimer);
         this._areaTimer.stop();
         this._areaTimer = null;
         this.icon = null;
         this.area = null;
         this.marker = null;
         super.onDispose();
      }
      
      override protected function initialize() : void
      {
         this._colorSchemeMgr.addEventListener(ColorSchemeEvent.SCHEMAS_UPDATED,this.onSchemasUpdatedHandler);
         this.updateColorBlind();
         super.initialize();
         this.setColor();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(InvalidationType.STATE))
         {
            this.setColor();
         }
      }
      
      protected function setColor() : void
      {
         var _loc2_:ColorTransform = null;
         var _loc1_:ColorTransform = this.marker.transform.colorTransform;
         _loc2_ = this.area.transform.colorTransform;
         _loc1_.color = this.getColor();
         _loc2_.color = this.getColor();
         this.alpha = this.getAlpha();
         this.marker.transform.colorTransform = _loc1_;
         this.area.transform.colorTransform = _loc2_;
      }
      
      protected function getAlpha() : Number
      {
         switch(this._timerCounter)
         {
            case 0:
               return FULL_ALPHA;
            case 1:
               return FIRST_ALPHA;
            case 2:
               return SECOND_ALPHA;
            case 3:
               return THIRD_ALPHA;
            default:
               return LAST_ALPHA;
         }
      }
      
      protected function getColor() : uint
      {
         if(this._isAlly)
         {
            return ALLY_COLOR;
         }
         if(this.colorblindMode)
         {
            return COLORBLIND_COLOR;
         }
         return ENEMY_COLOR;
      }
      
      public function setIsAlly(param1:Boolean) : void
      {
         this._isAlly = param1;
         invalidateState();
      }
      
      protected function setColorBlindMode(param1:Boolean) : void
      {
         if(this.colorblindMode != param1)
         {
            this.colorblindMode = param1;
            invalidateState();
         }
      }
      
      protected function updateColorBlind() : void
      {
         this.setColorBlindMode(this._colorSchemeMgr.getIsColorBlindS());
      }
      
      private function onSchemasUpdatedHandler(param1:ColorSchemeEvent) : void
      {
         this.updateColorBlind();
      }
   }
}
