package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.infrastructure.base.BaseDAAPIComponent;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class PlayerSatisfactionWidgetMeta extends BaseDAAPIComponent
   {
       
      
      public var selectedChoice:Function;
      
      private var _array:Array;
      
      private var _array1:Array;
      
      public function PlayerSatisfactionWidgetMeta()
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
      
      public function selectedChoiceS(param1:int) : void
      {
         App.utils.asserter.assertNotNull(this.selectedChoice,"selectedChoice" + Errors.CANT_NULL);
         this.selectedChoice(param1);
      }
      
      public final function as_setInitData(param1:Array, param2:Array, param3:int) : void
      {
         var _loc4_:Array = this._array;
         this._array = param1;
         var _loc5_:Array = this._array1;
         this._array1 = param2;
         this.setInitData(this._array,this._array1,param3);
         if(_loc4_)
         {
            _loc4_.splice(0,_loc4_.length);
         }
         if(_loc5_)
         {
            _loc5_.splice(0,_loc5_.length);
         }
      }
      
      protected function setInitData(param1:Array, param2:Array, param3:int) : void
      {
         var _loc4_:String = "as_setInitData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc4_);
         throw new AbstractException(_loc4_);
      }
   }
}
