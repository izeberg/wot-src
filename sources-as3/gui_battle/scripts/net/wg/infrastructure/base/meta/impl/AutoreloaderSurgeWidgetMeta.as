package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.views.widgetsPanel.BaseVehicleMechanicsWidget;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class AutoreloaderSurgeWidgetMeta extends BaseVehicleMechanicsWidget
   {
       
      
      private var _array:Array;
      
      public function AutoreloaderSurgeWidgetMeta()
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
         super.onDispose();
      }
      
      public final function as_setStagesProgress(param1:Array) : void
      {
         var _loc2_:Array = this._array;
         this._array = param1;
         this.setStagesProgress(this._array);
         if(_loc2_)
         {
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      protected function setStagesProgress(param1:Array) : void
      {
         var _loc2_:String = "as_setStagesProgress" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
