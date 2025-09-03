package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.gui.battle.views.widgetsPanel.vo.HotKeyVo;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class BaseVehicleMechanicsWidgetMeta extends BattleDisplayable
   {
       
      
      private var _vectorHotKeyVo:Vector.<HotKeyVo>;
      
      public function BaseVehicleMechanicsWidgetMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:HotKeyVo = null;
         if(this._vectorHotKeyVo)
         {
            for each(_loc1_ in this._vectorHotKeyVo)
            {
               _loc1_.dispose();
            }
            this._vectorHotKeyVo.splice(0,this._vectorHotKeyVo.length);
            this._vectorHotKeyVo = null;
         }
         super.onDispose();
      }
      
      public final function as_setHotKeys(param1:Array) : void
      {
         var _loc5_:HotKeyVo = null;
         var _loc2_:Vector.<HotKeyVo> = this._vectorHotKeyVo;
         this._vectorHotKeyVo = new Vector.<HotKeyVo>(0);
         var _loc3_:uint = param1.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc3_)
         {
            this._vectorHotKeyVo[_loc4_] = new HotKeyVo(param1[_loc4_]);
            _loc4_++;
         }
         this.setHotKeys(this._vectorHotKeyVo);
         if(_loc2_)
         {
            for each(_loc5_ in _loc2_)
            {
               _loc5_.dispose();
            }
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      protected function setHotKeys(param1:Vector.<HotKeyVo>) : void
      {
         var _loc2_:String = "as_setHotKeys" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
