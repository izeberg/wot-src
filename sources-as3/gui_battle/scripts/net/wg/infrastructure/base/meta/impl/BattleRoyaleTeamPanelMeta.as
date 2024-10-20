package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class BattleRoyaleTeamPanelMeta extends BattleDisplayable
   {
       
      
      private var _array:Array;
      
      private var _array1:Array;
      
      public function BattleRoyaleTeamPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._array)
         {
            this._array.splice(0,this._array.length);
            this._array = null;
         }
         if(this._array1)
         {
            this._array1.splice(0,this._array1.length);
            this._array1 = null;
         }
         super.onDispose();
      }
      
      public final function as_setInitData(param1:String, param2:Array, param3:Array, param4:int) : void
      {
         var _loc5_:Array = this._array;
         this._array = param2;
         var _loc6_:Array = this._array1;
         this._array1 = param3;
         this.setInitData(param1,this._array,this._array1,param4);
         if(_loc5_)
         {
            _loc5_.splice(0,_loc5_.length);
         }
         if(_loc6_)
         {
            _loc6_.splice(0,_loc6_.length);
         }
      }
      
      protected function setInitData(param1:String, param2:Array, param3:Array, param4:int) : void
      {
         var _loc5_:String = "as_setInitData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc5_);
         throw new AbstractException(_loc5_);
      }
   }
}
