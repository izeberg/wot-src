package net.wg.historical_battles.gui.battle.views.spgPanel
{
   import flash.events.Event;
   import flash.text.TextField;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.historical_battles.gui.battle.components.HBVehicleType;
   import net.wg.historical_battles.gui.battle.views.playersPanel.components.healthBar.HBHealthBar;
   import net.wg.historical_battles.gui.battle.views.spgPanel.VO.HBSPGInfoVO;
   
   public class HBSPGRenderer extends BattleUIComponent
   {
      
      private static const ALIVE_STATE:String = "alive";
      
      private static const DEAD_STATE:String = "dead";
       
      
      public var icon:BattleAtlasSprite = null;
      
      public var vehicleType:HBVehicleType = null;
      
      public var vehicleDescTF:TextField = null;
      
      public var healthBar:HBHealthBar = null;
      
      private var _data:HBSPGInfoVO = null;
      
      private var _isSkipAnimation:Boolean = true;
      
      private var _state:String;
      
      public function HBSPGRenderer()
      {
         super();
         this.icon.isCentralize = true;
      }
      
      override protected function draw() : void
      {
         var _loc1_:String = null;
         var _loc2_:Boolean = false;
         if(!this._data)
         {
            return;
         }
         if(isInvalid(InvalidationType.DATA))
         {
            _loc1_ = this._data.hpCurrent > 0 ? ALIVE_STATE : DEAD_STATE;
            if(this._state != _loc1_)
            {
               this._state = _loc1_;
               _loc2_ = this._state == ALIVE_STATE;
               this.gotoAndStop(this._state);
               this.vehicleType.vehicleType = this._data.vehicleType;
               this.vehicleType.alpha = !!_loc2_ ? Number(1) : Number(0.5);
               this.vehicleDescTF.text = this._data.vehicleName;
               this.icon.imageName = !!_loc2_ ? BATTLEATLAS.HB_SPG_DEFENCE : BATTLEATLAS.HB_SPG_DEFENCE_DEAD;
            }
            this.healthBar.updateHp(this._data.hpMax,this._data.hpCurrent,this._isSkipAnimation);
         }
      }
      
      override protected function onDispose() : void
      {
         this.vehicleType.dispose();
         this.vehicleType = null;
         this.icon = null;
         this.healthBar.dispose();
         this.healthBar = null;
         if(this._data)
         {
            this._data.removeEventListener(Event.CHANGE,this.onDataChangeHandler);
            this._data = null;
         }
         this.vehicleDescTF = null;
         super.onDispose();
      }
      
      public function setHp(param1:int, param2:int) : void
      {
         if(!this._data)
         {
            return;
         }
         this._data.hpCurrent = param2;
         this._data.hpMax = param1;
         this._isSkipAnimation = false;
         invalidateData();
      }
      
      public function set data(param1:HBSPGInfoVO) : void
      {
         if(this._data == param1)
         {
            return;
         }
         if(this._data)
         {
            this._data.removeEventListener(Event.CHANGE,this.onDataChangeHandler);
         }
         this._data = param1;
         this._data.addEventListener(Event.CHANGE,this.onDataChangeHandler);
         this._isSkipAnimation = true;
         invalidateData();
      }
      
      public function get vehicleID() : int
      {
         return Boolean(this._data) ? int(this._data.vehicleID) : int(0);
      }
      
      private function onDataChangeHandler(param1:Event) : void
      {
         invalidateData();
      }
   }
}
