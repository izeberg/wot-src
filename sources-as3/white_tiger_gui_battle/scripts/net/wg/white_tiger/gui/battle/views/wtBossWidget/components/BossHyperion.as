package net.wg.white_tiger.gui.battle.views.wtBossWidget.components
{
   import net.wg.gui.battle.components.BattleUIComponent;
   import net.wg.gui.components.controls.TextFieldContainer;
   import net.wg.white_tiger.data.constants.WT_VEHICLE_TYPE;
   
   public class BossHyperion extends BattleUIComponent
   {
       
      
      public var hyperionTF:TextFieldContainer = null;
      
      private var _bossType:String = "boss";
      
      public function BossHyperion()
      {
         super();
      }
      
      private static function getFrameLabel(param1:Boolean, param2:Boolean, param3:String) : String
      {
         return "hyperion_" + getStatePostfix(param1) + "_shield_" + getStatePostfix(param2) + "_" + getBossPostfix(param3);
      }
      
      private static function getStatePostfix(param1:Boolean) : String
      {
         return !!param1 ? "on" : "off";
      }
      
      private static function getBossPostfix(param1:String) : String
      {
         return param1 == WT_VEHICLE_TYPE.BOSS ? WT_VEHICLE_TYPE.BOSS : WT_VEHICLE_TYPE.BOSS_2025;
      }
      
      override protected function onDispose() : void
      {
         this.hyperionTF = null;
         super.onDispose();
      }
      
      public function updateHyperionCharge(param1:Number, param2:Number, param3:Boolean) : void
      {
         var _loc4_:Boolean = param1 / param2 >= 1;
         gotoAndStop(getFrameLabel(_loc4_,param3,this._bossType));
         if(this.hyperionTF)
         {
            this.hyperionTF.label = param1 + "%";
         }
      }
      
      public function set bossType(param1:String) : void
      {
         if(this._bossType != param1)
         {
            this._bossType = param1;
         }
      }
   }
}
