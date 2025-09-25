package net.wg.frontline.gui.battle.views.upgradePanel.data
{
   import net.wg.data.constants.Errors;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.battle.windows.vo.IngameDetailsKeyVO;
   
   public class FrontlineModuleInfoVO extends DAAPIDataClass
   {
      
      private static const MODULE_LABEL:String = "module";
      
      private static const HOTKEY_LABEL:String = "hotKeys";
       
      
      public var header:String = "";
      
      public var description:String = "";
      
      public var category:String = "";
      
      public var module:FrontlineConfiguratorModuleVO = null;
      
      public var hotKeys:Vector.<IngameDetailsKeyVO>;
      
      public function FrontlineModuleInfoVO(param1:Object = null)
      {
         this.hotKeys = new Vector.<IngameDetailsKeyVO>();
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Array = null;
         var _loc4_:Object = null;
         if(param1 == MODULE_LABEL)
         {
            if(this.module)
            {
               this.module.dispose();
            }
            this.module = new FrontlineConfiguratorModuleVO(param2);
            return false;
         }
         if(param1 == HOTKEY_LABEL)
         {
            this.clearHotKeys();
            _loc3_ = param2 as Array;
            if(_loc3_)
            {
               for each(_loc4_ in _loc3_)
               {
                  this.hotKeys.push(new IngameDetailsKeyVO(_loc4_));
               }
            }
            else
            {
               App.utils.asserter.assert(false,Errors.INVALID_TYPE + Array);
            }
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         this.clearHotKeys();
         this.hotKeys = null;
         this.module.dispose();
         this.module = null;
         super.onDispose();
      }
      
      private function clearHotKeys() : void
      {
         var _loc1_:IngameDetailsKeyVO = null;
         for each(_loc1_ in this.hotKeys)
         {
            _loc1_.dispose();
         }
         this.hotKeys.splice(0,this.hotKeys.length);
      }
   }
}
