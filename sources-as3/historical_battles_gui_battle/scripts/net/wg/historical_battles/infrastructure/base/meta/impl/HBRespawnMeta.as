package net.wg.historical_battles.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBRespawnVO;
   import net.wg.historical_battles.gui.battle.views.respawn.data.HBTimerRespVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class HBRespawnMeta extends BattleDisplayable
   {
       
      
      public var onPickVehicle:Function;
      
      public var onSelectVehicle:Function;
      
      private var _hBRespawnVO:HBRespawnVO;
      
      private var _hBTimerRespVO:HBTimerRespVO;
      
      public function HBRespawnMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._hBRespawnVO)
         {
            this._hBRespawnVO.dispose();
            this._hBRespawnVO = null;
         }
         if(this._hBTimerRespVO)
         {
            this._hBTimerRespVO.dispose();
            this._hBTimerRespVO = null;
         }
         super.onDispose();
      }
      
      public function onPickVehicleS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.onPickVehicle,"onPickVehicle" + Errors.CANT_NULL);
         this.onPickVehicle(param1);
      }
      
      public function onSelectVehicleS() : void
      {
         App.utils.asserter.assertNotNull(this.onSelectVehicle,"onSelectVehicle" + Errors.CANT_NULL);
         this.onSelectVehicle();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:HBRespawnVO = this._hBRespawnVO;
         this._hBRespawnVO = new HBRespawnVO(param1);
         this.setData(this._hBRespawnVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_setTimerData(param1:Object) : void
      {
         var _loc2_:HBTimerRespVO = this._hBTimerRespVO;
         this._hBTimerRespVO = new HBTimerRespVO(param1);
         this.setTimerData(this._hBTimerRespVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function setData(param1:HBRespawnVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function setTimerData(param1:HBTimerRespVO) : void
      {
         var _loc2_:String = "as_setTimerData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
