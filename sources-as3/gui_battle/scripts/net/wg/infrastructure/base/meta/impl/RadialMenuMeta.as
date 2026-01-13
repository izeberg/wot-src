package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class RadialMenuMeta extends BattleDisplayable
   {
       
      
      public var onSelect:Function;
      
      public var onAction:Function;
      
      public var onHideCompleted:Function;
      
      public var onRefresh:Function;
      
      private var _array:Array;
      
      private var _array1:Array;
      
      private var _array2:Array;
      
      private var _array3:Array;
      
      public function RadialMenuMeta()
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
         if(this._array2)
         {
            this._array2.splice(0,this._array2.length);
            this._array2 = null;
         }
         if(this._array3)
         {
            this._array3.splice(0,this._array3.length);
            this._array3 = null;
         }
         super.onDispose();
      }
      
      public function onSelectS() : void
      {
         App.utils.asserter.assertNotNull(this.onSelect,"onSelect" + Errors.CANT_NULL);
         this.onSelect();
      }
      
      public function onActionS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onAction,"onAction" + Errors.CANT_NULL);
         this.onAction(param1);
      }
      
      public function onHideCompletedS() : void
      {
         App.utils.asserter.assertNotNull(this.onHideCompleted,"onHideCompleted" + Errors.CANT_NULL);
         this.onHideCompleted();
      }
      
      public function onRefreshS() : void
      {
         App.utils.asserter.assertNotNull(this.onRefresh,"onRefresh" + Errors.CANT_NULL);
         this.onRefresh();
      }
      
      public final function as_buildData(param1:Array) : void
      {
         var _loc2_:Array = this._array;
         this._array = param1;
         this.buildData(this._array);
         if(_loc2_)
         {
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      public final function as_show(param1:Number, param2:Number, param3:String, param4:Array, param5:Array, param6:Array) : void
      {
         var _loc7_:Array = this._array1;
         this._array1 = param4;
         var _loc8_:Array = this._array2;
         this._array2 = param5;
         var _loc9_:Array = this._array3;
         this._array3 = param6;
         this.show(param1,param2,param3,this._array1,this._array2,this._array3);
         if(_loc7_)
         {
            _loc7_.splice(0,_loc7_.length);
         }
         if(_loc8_)
         {
            _loc8_.splice(0,_loc8_.length);
         }
         if(_loc9_)
         {
            _loc9_.splice(0,_loc9_.length);
         }
      }
      
      protected function buildData(param1:Array) : void
      {
         var _loc2_:String = "as_buildData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function show(param1:Number, param2:Number, param3:String, param4:Array, param5:Array, param6:Array) : void
      {
         var _loc7_:String = "as_show" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc7_);
         throw new AbstractException(_loc7_);
      }
   }
}
