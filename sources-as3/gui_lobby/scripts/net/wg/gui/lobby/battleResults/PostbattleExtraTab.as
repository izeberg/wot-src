package net.wg.gui.lobby.battleResults
{
   import flash.display.InteractiveObject;
   import net.wg.data.Aliases;
   import net.wg.gui.lobby.battleResults.postbattleExtraTab.PostbattleExtraTabContent;
   import net.wg.infrastructure.base.UIComponentEx;
   import net.wg.infrastructure.base.meta.IBaseDAAPIComponentMeta;
   import net.wg.infrastructure.interfaces.IRegisteredComponent;
   import net.wg.infrastructure.interfaces.IViewStackContent;
   
   public class PostbattleExtraTab extends UIComponentEx implements IViewStackContent, IRegisteredComponent
   {
       
      
      public var content:PostbattleExtraTabContent = null;
      
      private var _register:IBaseDAAPIComponentMeta;
      
      public function PostbattleExtraTab()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         this.content.width = width;
         this.content.height = height;
      }
      
      override protected function onDispose() : void
      {
         this._register.unregisterFlashComponentS(Aliases.POSTBATTLE_EXTRA_TAB);
         this._register = null;
         this.content = null;
         super.onDispose();
      }
      
      public function canShowAutomatically() : Boolean
      {
         return true;
      }
      
      public function getComponentForFocus() : InteractiveObject
      {
         return null;
      }
      
      public function registerFlashComponentVia(param1:IBaseDAAPIComponentMeta) : void
      {
         if(!param1.isFlashComponentRegisteredS(Aliases.POSTBATTLE_EXTRA_TAB))
         {
            this._register = param1;
            param1.registerFlashComponentS(this.content,Aliases.POSTBATTLE_EXTRA_TAB);
         }
      }
      
      public function update(param1:Object) : void
      {
      }
   }
}
