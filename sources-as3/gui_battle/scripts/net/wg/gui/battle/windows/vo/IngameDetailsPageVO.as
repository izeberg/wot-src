package net.wg.gui.battle.windows.vo
{
   import net.wg.data.constants.Values;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class IngameDetailsPageVO extends DAAPIDataClass
   {
      
      private static const ROLE_ACTIONS_FIELD_NAME:String = "roleActions";
      
      private static const KEYS_FIELD_NAME:String = "keys";
       
      
      public var headerTitle:String = "";
      
      public var title:String = "";
      
      public var descr:String = "";
      
      public var image:String = "";
      
      public var roleImage:String = "";
      
      private var _roleActions:Vector.<IngameDetailsRoleActionVO> = null;
      
      private var _keys:Vector.<IngameDetailsKeyVO> = null;
      
      public function IngameDetailsPageVO(param1:Object = null)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == ROLE_ACTIONS_FIELD_NAME)
         {
            if(param2 is Array)
            {
               this._roleActions = Vector.<IngameDetailsRoleActionVO>(App.utils.data.convertVOArrayToVector(param1,param2,IngameDetailsRoleActionVO));
            }
            return false;
         }
         if(param1 == KEYS_FIELD_NAME)
         {
            if(param2 is Array)
            {
               this.clearHotKeys();
               this._keys = Vector.<IngameDetailsKeyVO>(App.utils.data.convertVOArrayToVector(param1,param2,IngameDetailsKeyVO));
            }
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IDisposable = null;
         this.clearHotKeys();
         this._keys = null;
         if(this._roleActions != null)
         {
            for each(_loc1_ in this._roleActions)
            {
               _loc1_.dispose();
            }
            this._roleActions.splice(0,this._roleActions.length);
            this._roleActions = null;
         }
         super.onDispose();
      }
      
      private function clearHotKeys() : void
      {
         var _loc1_:IngameDetailsKeyVO = null;
         if(this._keys)
         {
            for each(_loc1_ in this._keys)
            {
               _loc1_.dispose();
            }
            this._keys.splice(0,this._keys.length);
         }
      }
      
      public function get hasEmptyKey() : Boolean
      {
         var _loc1_:IngameDetailsKeyVO = null;
         for each(_loc1_ in this._keys)
         {
            if(_loc1_.keyName == Values.EMPTY_STR)
            {
               return true;
            }
         }
         return false;
      }
      
      public function get roleActions() : Vector.<IngameDetailsRoleActionVO>
      {
         return this._roleActions;
      }
      
      public function get keys() : Vector.<IngameDetailsKeyVO>
      {
         return this._keys;
      }
   }
}
