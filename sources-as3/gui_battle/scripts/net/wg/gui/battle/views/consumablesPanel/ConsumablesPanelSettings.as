package net.wg.gui.battle.views.consumablesPanel
{
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   
   public class ConsumablesPanelSettings implements IDisposable
   {
       
      
      public var bottomPadding:int = 0;
      
      public var itemPadding:int = 0;
      
      public var groupGap:int = 0;
      
      public var customIndexGap:Vector.<uint>;
      
      public var equipmentButtonLinkage:String = "";
      
      public var shellButtonLinkage:String = "";
      
      private var _disposed:Boolean = false;
      
      public function ConsumablesPanelSettings(param1:int, param2:int, param3:String, param4:String, param5:int = 0, param6:Vector.<uint> = null)
      {
         this.customIndexGap = new Vector.<uint>(0);
         super();
         this.bottomPadding = param1;
         this.itemPadding = param2;
         this.groupGap = param5;
         if(param6 != null)
         {
            this.customIndexGap = param6;
         }
         this.equipmentButtonLinkage = param3;
         this.shellButtonLinkage = param4;
      }
      
      public final function dispose() : void
      {
         this._disposed = true;
         this.onDispose();
      }
      
      public function isDisposed() : Boolean
      {
         return this._disposed;
      }
      
      protected function onDispose() : void
      {
         this.customIndexGap.splice(0,this.customIndexGap.length);
         this.customIndexGap = null;
      }
   }
}
