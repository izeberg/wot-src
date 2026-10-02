package net.wg.portal.gui.battle.fullStats.components
{
   import flash.text.TextField;
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.battleRoyale.data.DescriptionBlockWithIconVO;
   import net.wg.gui.battle.components.BattleAtlasSprite;
   import net.wg.infrastructure.base.SimpleDisposable;
   import net.wg.infrastructure.interfaces.entity.IUpdatable;
   
   public class DescriptionWithIconRenderer extends SimpleDisposable implements IUpdatable
   {
      
      private static const ICON_SCALE:Number = 0.5;
       
      
      public var icon:BattleAtlasSprite = null;
      
      public var descriptionTF:TextField = null;
      
      protected var iconPostfix:String = "";
      
      public function DescriptionWithIconRenderer()
      {
         super();
         this.icon.isCentralize = true;
         this.icon.isSmoothingEnabled = true;
         this.icon.scaleX = this.icon.scaleY = ICON_SCALE;
      }
      
      override protected function onDispose() : void
      {
         this.icon = null;
         this.descriptionTF = null;
         super.onDispose();
      }
      
      public function update(param1:Object) : void
      {
         var _loc2_:DescriptionBlockWithIconVO = null;
         if(param1 != null)
         {
            _loc2_ = param1 as DescriptionBlockWithIconVO;
            if(_loc2_ != null)
            {
               if(this.descriptionTF)
               {
                  this.descriptionTF.text = _loc2_.description;
               }
               this.icon.imageName = _loc2_.icon + this.iconPostfix;
               this.icon.blendMode = _loc2_.blendMode;
            }
            else
            {
               App.utils.asserter.assert(false,Errors.INVALID_TYPE + DescriptionBlockWithIconVO);
            }
            App.utils.commons.updateTextFieldSize(this.descriptionTF);
            this.descriptionTF.y = this.icon.y - (this.descriptionTF.height >> 1);
         }
      }
   }
}
